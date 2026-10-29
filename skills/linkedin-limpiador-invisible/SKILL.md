---
name: linkedin-limpiador-invisible
description: Borra los caracteres invisibles y espacios raros que quedan en un texto al copiarlo de herramientas de IA, editores o webs (espacios de ancho cero, marcas de dirección, caracteres ocultos), antes de publicarlo en LinkedIn. Úsala cuando pida limpiar un texto, quitar caracteres ocultos o preparar un post para publicar.
---

# Limpiador de caracteres invisibles

Al copiar texto desde una herramienta de IA, un documento o una web, a veces viajan caracteres que no se ven: espacios de ancho cero, marcas de dirección, guiones suaves, espacios de no separación o caracteres "tag" que pueden esconder texto. No se ven en pantalla, pero sí los detectan las herramientas que analizan texto, rompen el formato en LinkedIn y a veces cortan palabras raro.

Esta skill los encuentra, los borra y te dice cuántos había de cada tipo.

## Cómo usarla

1. Guarda el texto del usuario en un archivo (por ejemplo `post.txt`), sin modificarlo.
2. Corre el script incluido:
   ```bash
   python scripts/limpiar.py post.txt --json
   ```
   Opciones:
   - `--guiones` también reemplaza los guiones largos (—, –) por comas. Úsala si el usuario lo pide o si el texto se va a publicar en LinkedIn y él no los usa a propósito.
3. Del JSON, toma `texto` (limpio) y `reporte`.

Si no hay herramienta para correr código, haz la limpieza a mano revisando estos caracteres: U+200B–U+200F, U+202A–U+202E, U+2060–U+2064, U+2066–U+206F, U+FEFF, U+00AD, U+180E, U+E0000–U+E007F (se borran) y U+00A0, U+202F, U+2000–U+200A, U+3000 (se cambian por un espacio normal). Aclara que fue una revisión manual.

## Entrega

1. El reporte: qué se encontró y cuántos de cada tipo. Si no había nada, dilo: "estaba limpio".
2. El texto limpio, completo, listo para copiar.

## Qué NO hace

- No reescribe ni cambia palabras (eso es `linkedin-humanizador`).
- No toca los emojis: los selectores de variación y modificadores de tono de piel que van pegados a un emoji se mantienen.
- No hace que un texto "no parezca IA" por sí sola: quita rastros técnicos de copiar y pegar. Para el estilo, usa `linkedin-humanizador` y después `linkedin-detector-ia`.
