#!/usr/bin/env python3
"""
Limpia caracteres invisibles o raros que quedan al copiar texto de herramientas de IA,
editores o webs: espacios de ancho cero, marcas de dirección, guiones suaves,
caracteres "tag", espacios no estándar, etc.

Uso:
  python limpiar.py archivo.txt            -> imprime el texto limpio
  python limpiar.py archivo.txt --reporte  -> imprime el texto limpio y un reporte en stderr
  echo "texto" | python limpiar.py -       -> lee de stdin
  python limpiar.py archivo.txt --json     -> {"texto": ..., "cambios": {...}}

Solo usa la librería estándar.
"""
from __future__ import annotations

import json
import sys
import unicodedata

# Se eliminan
INVISIBLES = {
    "​": "espacio de ancho cero (U+200B)",
    "‌": "separador de ancho cero (U+200C)",
    "‍": "unión de ancho cero (U+200D)",
    "⁠": "unión de palabra (U+2060)",
    "﻿": "marca BOM / ZWNBSP (U+FEFF)",
    "᠎": "separador de vocal mongol (U+180E)",
    "­": "guion suave (U+00AD)",
    "‎": "marca izquierda-a-derecha (U+200E)",
    "‏": "marca derecha-a-izquierda (U+200F)",
    "؜": "marca de letra árabe (U+061C)",
    "⁡": "aplicación de función invisible (U+2061)",
    "⁢": "multiplicación invisible (U+2062)",
    "⁣": "separador invisible (U+2063)",
    "⁤": "suma invisible (U+2064)",
    "͏": "unión de grafemas (U+034F)",
}
for cp in range(0x202A, 0x202F):
    INVISIBLES[chr(cp)] = f"control de dirección (U+{cp:04X})"
for cp in range(0x2066, 0x206A):
    INVISIBLES[chr(cp)] = f"aislamiento de dirección (U+{cp:04X})"
for cp in range(0x206A, 0x2070):
    INVISIBLES[chr(cp)] = f"formato obsoleto (U+{cp:04X})"

# Se reemplazan por un espacio normal
ESPACIOS = {
    " ": "espacio de no separación (U+00A0)",
    " ": "espacio angosto de no separación (U+202F)",
    " ": "espacio de cifra (U+2007)",
    " ": "espacio de puntuación (U+2008)",
    " ": "espacio fino (U+2009)",
    " ": "espacio muy fino (U+200A)",
    " ": "espacio en (U+2002)",
    " ": "espacio em (U+2003)",
    " ": "espacio 1/3 em (U+2004)",
    " ": "espacio 1/4 em (U+2005)",
    " ": "espacio 1/6 em (U+2006)",
    " ": "espacio matemático (U+205F)",
    "　": "espacio ideográfico (U+3000)",
}

GUIONES = {"—": "guion largo (—)", "–": "guion medio (–)", "―": "barra horizontal (―)"}


def _es_tag(ch: str) -> bool:
    return 0xE0000 <= ord(ch) <= 0xE007F  # caracteres "tag": invisibles, pueden esconder texto


def _es_selector_variacion_suelto(texto: str, i: int) -> bool:
    """Los selectores de variación (FE00–FE0F, E0100–E01EF) son legítimos detrás de un emoji.
    Sueltos detrás de letras comunes no tienen función visible."""
    ch = texto[i]
    o = ord(ch)
    if not (0xFE00 <= o <= 0xFE0F or 0xE0100 <= o <= 0xE01EF):
        return False
    previo = texto[i - 1] if i > 0 else ""
    if not previo:
        return True
    cat = unicodedata.category(previo)
    # detrás de un símbolo o emoji (So) o de dígitos/#/* (keycaps) es normal
    return not (cat in ("So", "Sk", "Sm") or previo in "0123456789#*" or ord(previo) > 0x2000)


def limpiar(texto: str, guiones: bool = False) -> tuple[str, dict[str, int]]:
    cambios: dict[str, int] = {}

    def contar(nombre: str):
        cambios[nombre] = cambios.get(nombre, 0) + 1

    salida = []
    for i, ch in enumerate(texto):
        if ch in INVISIBLES:
            contar(INVISIBLES[ch])
            continue
        if _es_tag(ch):
            contar("carácter tag invisible (U+E00xx)")
            continue
        if _es_selector_variacion_suelto(texto, i):
            contar(f"selector de variación suelto (U+{ord(ch):04X})")
            continue
        if ch in ESPACIOS:
            contar(ESPACIOS[ch])
            salida.append(" ")
            continue
        if guiones and ch in GUIONES:
            contar(GUIONES[ch])
            salida.append("\u0000GUION\u0000")
            continue
        if unicodedata.category(ch) == "Cc" and ch not in "\n\t":
            if ch == "\r":
                continue  # normaliza saltos de línea de Windows sin reportarlo
            contar(f"carácter de control (U+{ord(ch):04X})")
            continue
        salida.append(ch)

    resultado = "".join(salida)
    if guiones:
        # " — " entre palabras -> ", " ; "palabra—palabra" -> "palabra, palabra"
        import re
        resultado = re.sub(r"\s*\u0000GUION\u0000\s*", ", ", resultado)
        resultado = re.sub(r",\s*,", ",", resultado)
        resultado = re.sub(r"^,\s*", "", resultado, flags=re.M)
    # espacios dobles creados por la limpieza (sin tocar la sangría al inicio de línea)
    import re
    resultado = re.sub(r"(?<=\S) {2,}", " ", resultado)
    resultado = re.sub(r" +\n", "\n", resultado)
    return resultado, cambios


def reporte(cambios: dict[str, int]) -> str:
    if not cambios:
        return "Texto limpio: no había caracteres invisibles ni raros."
    total = sum(cambios.values())
    lineas = [f"Se limpiaron {total} caracteres:"]
    for nombre, n in sorted(cambios.items(), key=lambda kv: -kv[1]):
        lineas.append(f"  - {n} × {nombre}")
    return "\n".join(lineas)


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="Limpia caracteres invisibles de un texto")
    ap.add_argument("archivo", help="ruta del archivo o - para stdin")
    ap.add_argument("--guiones", action="store_true", help="también reemplaza guiones largos por comas")
    ap.add_argument("--reporte", action="store_true", help="muestra el reporte en stderr")
    ap.add_argument("--json", action="store_true", help="salida JSON con texto y cambios")
    a = ap.parse_args(argv)
    texto = sys.stdin.read() if a.archivo == "-" else open(a.archivo, encoding="utf-8").read()
    limpio, cambios = limpiar(texto, guiones=a.guiones)
    if a.json:
        print(json.dumps({"texto": limpio, "cambios": cambios, "reporte": reporte(cambios)}, ensure_ascii=False))
        return
    sys.stdout.write(limpio)
    if a.reporte:
        print("\n" + reporte(cambios), file=sys.stderr)


if __name__ == "__main__":
    main()
