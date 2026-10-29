#!/usr/bin/env python3
"""Valida cada skill y genera dist/<skill>.zip (uno por skill, listo para subir a Claude)
y dist/pack-linkedin-11-skills.zip (todos juntos)."""
import os, re, sys, zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(RAIZ, "skills")
DIST = os.path.join(RAIZ, "dist")


def validar(nombre):
    ruta = os.path.join(SKILLS, nombre, "SKILL.md")
    errores = []
    if not os.path.isfile(ruta):
        return [f"{nombre}: falta SKILL.md"]
    txt = open(ruta, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        return [f"{nombre}: falta el frontmatter"]
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    fm = {k.strip(): v.strip() for k, v in fm.items()}
    if fm.get("name") != nombre:
        errores.append(f"{nombre}: name '{fm.get('name')}' no coincide con la carpeta")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", nombre):
        errores.append(f"{nombre}: nombre inválido")
    d = fm.get("description", "")
    if not d or len(d) > 1024 or "<" in d or ">" in d:
        errores.append(f"{nombre}: description vacía, larga o con < >")
    return errores


def main():
    nombres = sorted(n for n in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, n)))
    errores = [e for n in nombres for e in validar(n)]
    if errores:
        print("\n".join(errores)); sys.exit(1)
    os.makedirs(DIST, exist_ok=True)
    for f in os.listdir(DIST):
        if f.endswith(".zip"):
            os.remove(os.path.join(DIST, f))
    for n in nombres:
        with zipfile.ZipFile(os.path.join(DIST, f"{n}.zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for base, _, archivos in os.walk(os.path.join(SKILLS, n)):
                if "__pycache__" in base:
                    continue
                for a in sorted(archivos):
                    p = os.path.join(base, a)
                    z.write(p, os.path.relpath(p, SKILLS))
    with zipfile.ZipFile(os.path.join(DIST, "pack-linkedin-11-skills.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for n in nombres:
            z.write(os.path.join(DIST, f"{n}.zip"), f"{n}.zip")
    print(f"OK: {len(nombres)} skills validadas y empaquetadas en dist/")


if __name__ == "__main__":
    main()
