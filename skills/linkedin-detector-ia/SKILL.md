---
name: linkedin-detector-ia
description: Pasa un post o texto por 5 pruebas de "suena a IA" (puntuación, vocabulario, ritmo, estructuras repetidas, formato) y dice exactamente qué corregir antes de publicarlo en LinkedIn. Úsala cuando pida revisar si un texto suena a IA, verificar un post antes de publicar o "pasarlo por el detector".
---

# Detector: 5 pruebas antes de publicar

Revisa el texto con las 5 pruebas y devuelve un puntaje por prueba, qué encontró y cómo arreglarlo.

| Prueba | Qué mira |
|---|---|
| 1. Puntuación delatora | Guiones largos usados como pausa, punto y coma, dos puntos en exceso |
| 2. Vocabulario de IA | Palabras y muletillas típicas de modelos ("en el panorama actual", "desbloquea", "crucial", "potencia tu", "delve", "leverage"…) |
| 3. Ritmo | Frases todas del mismo largo, sin frases cortas |
| 4. Estructuras repetidas | "No es X, es Y", enumeraciones de tres, frases que arrancan igual, listas con emoji al inicio |
| 5. Formato y limpieza | Caracteres invisibles, exceso de emojis, más de 5 hashtags, exclamaciones, negritas falsas |

Importante: son pruebas **heurísticas** de patrones conocidos. Sirven para sacar lo que más delata un texto generado; no son un detector oficial ni garantizan un resultado en herramientas externas. Dilo así si el usuario pregunta.

## Cómo usarla

1. Guarda el texto en un archivo sin modificarlo.
2. Corre:
   ```bash
   python scripts/detector.py post.txt
   ```
   (`--json` si necesitas procesar el resultado).
3. Si no hay herramienta para correr código, aplica las 5 pruebas a mano con la tabla de arriba y aclara que fue una revisión manual.

## Entrega

1. El reporte: puntaje total, cuántas de las 5 pruebas pasó, y por cada prueba que falló, los hallazgos concretos (las palabras exactas, las frases exactas).
2. Si falló 1 o más pruebas, ofrece la versión corregida aplicando las reglas de `linkedin-humanizador`, y vuelve a correr el detector sobre la versión nueva para mostrar el antes/después.
3. Si pasa las 5: "Listo para publicar". La decisión de publicar es del usuario.

No cambies el significado, los datos ni las historias del usuario al corregir.
