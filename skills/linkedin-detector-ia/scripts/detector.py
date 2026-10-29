#!/usr/bin/env python3
"""
Pasa un texto por 5 pruebas de "suena a IA" y devuelve un reporte con lo que hay que corregir.

Las 5 pruebas son heurísticas: detectan los patrones que más delatan un texto generado
(no son un detector oficial ni garantizan pasar herramientas externas).

  1. Puntuación delatora   - guiones largos, punto y coma, dos puntos en exceso
  2. Vocabulario de IA     - palabras y muletillas típicas de modelos de lenguaje (ES + EN)
  3. Ritmo                 - frases todas del mismo largo
  4. Estructuras repetidas - "no es X, es Y", tríadas, frases que arrancan igual, listas con emoji
  5. Formato y limpieza    - caracteres invisibles, exceso de emojis, hashtags, signos

Uso:
  python detector.py archivo.txt          -> reporte legible
  python detector.py archivo.txt --json   -> JSON
  echo "texto" | python detector.py -
Solo librería estándar.
"""
from __future__ import annotations

import json
import re
import statistics
import sys
import unicodedata

VOCABULARIO_IA = [
    # español
    "en el panorama actual", "en el mundo actual", "en la era digital", "en un mundo cada vez más",
    "sumergirse", "sumérgete", "adentrarse", "adentrémonos", "desbloquear", "desbloquea", "potenciar",
    "potencia tu", "aprovechar al máximo", "llevar al siguiente nivel", "lleva tu", "al siguiente nivel",
    "crucial", "fundamental", "esencial", "clave para", "es importante destacar", "cabe destacar",
    "cabe mencionar", "vale la pena mencionar", "en definitiva", "en resumen", "en conclusión",
    "transformador", "revolucionario", "innovador", "sin precedentes", "un antes y un después",
    "navegar por", "navegar el", "el viaje de", "tu viaje", "en constante evolución", "panorama",
    "ecosistema", "sinergia", "robusto", "integral", "holístico", "fomentar", "optimizar",
    "no se trata solo de", "no solo", "sino también", "juega un papel", "desempeña un papel",
    "a medida que", "es por eso que", "por lo tanto", "asimismo", "además de esto",
    "imagina un mundo", "¿alguna vez te has preguntado", "aquí te dejo", "te comparto",
    "espero que te sirva", "¡vamos!", "game changer", "en pocas palabras",
    # inglés
    "delve", "dive into", "unlock", "unleash", "leverage", "elevate", "game-changer", "game changer",
    "in today's", "ever-evolving", "landscape", "tapestry", "testament to", "seamless", "robust",
    "cutting-edge", "navigate", "journey", "crucial", "pivotal", "foster", "empower", "harness",
    "it's not just", "not only", "but also", "moreover", "furthermore", "in conclusion",
]

FRASES_CONTRASTE = [
    r"\bno es (?:solo |sólo |simplemente )?[^.,;\n]{1,40}[,;:]\s*(?:es|sino)\b",
    r"\bno se trata de [^.\n]{1,40}[,;]\s*se trata de\b",
    r"\bit'?s not (?:just |about )?[^.,;\n]{1,40}[,;—–-]\s*it'?s\b",
    r"\bno [a-záéíóúñ]+,\s*[a-záéíóúñ]+\.",
]

INVISIBLES = re.compile("[​-‏‪-‮⁠-⁤⁦-⁯﻿­᠎  \U000e0000-\U000e007f]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆✅❌]")


def _frases(texto: str) -> list[str]:
    partes = re.split(r"(?<=[.!?…])\s+|\n+", texto)
    return [p.strip() for p in partes if len(p.strip().split()) >= 2]


def _resultado(nombre, puntaje, hallazgos, consejo):
    return {"prueba": nombre, "puntaje": max(0, min(100, round(puntaje))), "aprobada": puntaje >= 70,
            "hallazgos": hallazgos, "consejo": consejo if puntaje < 70 else ""}


def prueba_puntuacion(texto: str):
    palabras = max(1, len(texto.split()))
    largos = texto.count("—") + texto.count("–") + len(re.findall(r"\s-\s", texto))
    pyc = texto.count(";")
    dos_puntos = len(re.findall(r":\s*\n|:\s+[A-ZÁÉÍÓÚ¿¡]", texto))
    hallazgos = []
    if largos:
        hallazgos.append(f"{largos} guion(es) largo(s) usados como pausa")
    if pyc:
        hallazgos.append(f"{pyc} punto(s) y coma")
    if dos_puntos > 2:
        hallazgos.append(f"{dos_puntos} dos puntos que introducen frases o listas")
    por_100 = 100 * (largos * 3 + pyc * 2 + max(0, dos_puntos - 2)) / palabras
    return _resultado("1. Puntuación delatora", 100 - por_100 * 12, hallazgos,
                      "Cambia los guiones largos por punto, coma o paréntesis. Evita el punto y coma.")


def prueba_vocabulario(texto: str):
    t = texto.lower()
    encontrados = []
    # de la expresión más larga a la más corta, para no contar "panorama" dentro de "en el panorama actual"
    for w in sorted(set(VOCABULARIO_IA), key=len, reverse=True):
        patron = r"(?<![\wáéíóúñ])" + re.escape(w) + r"(?![\wáéíóúñ])"
        n = len(re.findall(patron, t))
        if n:
            encontrados.append((w, n))
            t = re.sub(patron, " ", t)
    total = sum(n for _, n in encontrados)
    palabras = max(1, len(texto.split()))
    densidad = 100 * total / palabras
    hallazgos = [f"“{w}”" + (f" ×{n}" if n > 1 else "") for w, n in encontrados]
    return _resultado("2. Vocabulario de IA", 100 - densidad * 20 - max(0, total - 1) * 5, hallazgos,
                      "Reemplaza esas palabras por cómo lo dirías hablando. Si no lo dirías en una charla, sácalo.")


def prueba_ritmo(texto: str):
    frases = _frases(texto)
    if len(frases) < 4:
        return _resultado("3. Ritmo", 100, ["Texto corto: no se evalúa el ritmo"], "")
    largos = [len(f.split()) for f in frases]
    media = statistics.mean(largos)
    cv = statistics.pstdev(largos) / media if media else 0
    cortas = sum(1 for n in largos if n <= 6)
    hallazgos = [f"{len(frases)} frases, promedio {media:.0f} palabras, variación {cv:.2f}"]
    puntaje = 100
    if cv < 0.45:
        puntaje -= (0.45 - cv) * 160
        hallazgos.append("Las frases tienen casi todas el mismo largo")
    if cortas == 0:
        puntaje -= 20
        hallazgos.append("No hay ninguna frase corta (6 palabras o menos)")
    if media > 24:
        puntaje -= 15
        hallazgos.append("Frases largas en promedio")
    return _resultado("3. Ritmo", puntaje, hallazgos,
                      "Mezcla frases muy cortas con otras largas. Una frase de 3 palabras después de una de 25 suena humano.")


def prueba_estructuras(texto: str):
    hallazgos = []
    puntaje = 100
    t = texto.lower()
    contrastes = sum(len(re.findall(p, t)) for p in FRASES_CONTRASTE)
    if contrastes:
        hallazgos.append(f"{contrastes} estructura(s) “no es X, es Y”")
        puntaje -= 20 * contrastes
    triadas = len(re.findall(r"\b\w+(?: \w+)?, \w+(?: \w+)? y \w+", t))
    if triadas >= 2:
        hallazgos.append(f"{triadas} enumeraciones de tres (“X, Y y Z”)")
        puntaje -= 10 * (triadas - 1)
    frases = _frases(texto)
    inicios = {}
    for f in frases:
        k = " ".join(f.lower().split()[:2])
        inicios[k] = inicios.get(k, 0) + 1
    repetidos = {k: n for k, n in inicios.items() if n >= 3}
    for k, n in repetidos.items():
        hallazgos.append(f"{n} frases empiezan con “{k}”")
        puntaje -= 10 * (n - 2)
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    con_emoji = sum(1 for l in lineas if EMOJI.match(l))
    if con_emoji >= 3:
        hallazgos.append(f"{con_emoji} líneas empiezan con emoji (formato lista de IA)")
        puntaje -= 8 * con_emoji
    preguntas_retoricas = len(re.findall(r"¿[^?]{3,80}\?\s*(?:\n|$)", texto))
    if preguntas_retoricas >= 3:
        hallazgos.append(f"{preguntas_retoricas} preguntas retóricas")
        puntaje -= 10
    return _resultado("4. Estructuras repetidas", puntaje, hallazgos,
                      "Rompe los patrones: cambia el “no es X, es Y” por una afirmación directa y varía cómo empiezan las frases.")


def prueba_formato(texto: str):
    hallazgos = []
    puntaje = 100
    inv = len(INVISIBLES.findall(texto))
    if inv:
        hallazgos.append(f"{inv} carácter(es) invisible(s) o espacios raros")
        puntaje -= 40
    emojis = len(EMOJI.findall(texto))
    palabras = max(1, len(texto.split()))
    if emojis > max(3, palabras / 40):
        hallazgos.append(f"{emojis} emojis")
        puntaje -= 20
    hashtags = len(re.findall(r"(?<!\w)#\w+", texto))
    if hashtags > 5:
        hallazgos.append(f"{hashtags} hashtags (más de 5)")
        puntaje -= 15
    excl = texto.count("!")
    if excl > 3:
        hallazgos.append(f"{excl} signos de exclamación")
        puntaje -= 10
    negritas = len(re.findall(r"\*\*[^*]+\*\*", texto)) + sum(
        1 for ch in texto if unicodedata.name(ch, "").startswith("MATHEMATICAL BOLD"))
    if negritas:
        hallazgos.append("Negritas con ** o letras Unicode “bold” (LinkedIn no tiene negrita nativa)")
        puntaje -= 15
    comillas = set(re.findall(r"[\"“”«»]", texto))
    if len(comillas) >= 3:
        hallazgos.append("Tipos de comillas mezclados")
        puntaje -= 5
    return _resultado("5. Formato y limpieza", puntaje, hallazgos,
                      "Pasa el texto por linkedin-limpiador-invisible, deja 0–2 emojis y como mucho 3 hashtags.")


PRUEBAS = [prueba_puntuacion, prueba_vocabulario, prueba_ritmo, prueba_estructuras, prueba_formato]


def analizar(texto: str) -> dict:
    resultados = [p(texto) for p in PRUEBAS]
    total = round(sum(r["puntaje"] for r in resultados) / len(resultados))
    aprobadas = sum(r["aprobada"] for r in resultados)
    if aprobadas == 5:
        veredicto = "Suena humano. Listo para publicar."
    elif aprobadas >= 3:
        veredicto = "Casi. Corrige las pruebas marcadas antes de publicar."
    else:
        veredicto = "Suena a IA. Reescríbelo con linkedin-humanizador."
    return {"puntaje_total": total, "aprobadas": aprobadas, "veredicto": veredicto, "pruebas": resultados}


def formatear(r: dict) -> str:
    out = [f"Puntaje: {r['puntaje_total']}/100 · {r['aprobadas']}/5 pruebas aprobadas", r["veredicto"], ""]
    for p in r["pruebas"]:
        marca = "✓" if p["aprobada"] else "✗"
        out.append(f"{marca} {p['prueba']}: {p['puntaje']}/100")
        for h in p["hallazgos"]:
            out.append(f"    - {h}")
        if p["consejo"]:
            out.append(f"    → {p['consejo']}")
    return "\n".join(out)


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="5 pruebas de 'suena a IA'")
    ap.add_argument("archivo", help="ruta o - para stdin")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    texto = sys.stdin.read() if a.archivo == "-" else open(a.archivo, encoding="utf-8").read()
    r = analizar(texto)
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else formatear(r))


if __name__ == "__main__":
    main()
