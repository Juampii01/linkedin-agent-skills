---
name: linkedin-humanizador
description: Reescribe un texto para que suene escrito por una persona y no por una IA, quitando guiones largos, palabras típicas de IA y estructuras repetidas, sin cambiar lo que dice. Úsala cuando pida humanizar un texto, que "no suene a ChatGPT/IA", o antes de publicar un post generado con IA en LinkedIn.
---

# Humanizador

El objetivo no es engañar a nadie: es que el texto suene a ti. Las IA tienen tics de escritura que la gente ya reconoce y que hacen que dejen de leer. Esta skill los saca.

## Reglas de reescritura

### Puntuación
- Ningún guion largo (—) ni medio (–) como pausa. Reemplázalos por punto, coma o paréntesis, o reescribe la frase.
- Nada de punto y coma.
- Dos puntos solo si de verdad introducen una lista o un dato.

### Palabras que se van
Español: "en el panorama actual", "en el mundo actual", "en la era digital", "sumergirse", "adentrarse", "desbloquear", "potenciar", "aprovechar al máximo", "llevar al siguiente nivel", "crucial", "fundamental", "esencial", "cabe destacar", "en definitiva", "en resumen", "en conclusión", "transformador", "revolucionario", "sin precedentes", "navegar por", "ecosistema", "sinergia", "robusto", "holístico", "juega un papel", "imagina un mundo", "¿alguna vez te has preguntado…?".

Inglés: "delve", "unlock", "unleash", "leverage", "elevate", "game-changer", "in today's…", "ever-evolving", "landscape", "tapestry", "testament to", "seamless", "navigate", "journey", "pivotal", "foster", "empower", "harness", "moreover", "furthermore".

Reemplázalas por la palabra que usarías hablando, o borra la frase si no dice nada.

### Estructuras que se rompen
- "No es X, es Y" / "No se trata de X, se trata de Y" → afirma Y directamente.
- Enumeraciones de tres por reflejo ("rápido, simple y efectivo") → deja la que importa.
- Frases que empiezan igual → varía.
- Listas con un emoji al inicio de cada línea → texto corrido o lista sin emojis.
- Preguntas retóricas encadenadas → una como máximo.
- Cierres de manual ("Espero que te sirva", "¿Qué opinas? ¡Te leo en los comentarios!") → una pregunta concreta o nada.

### Ritmo y voz
- Mezcla frases cortas (3–6 palabras) con otras más largas.
- Primera persona y voz activa.
- Concreto en lugar de abstracto: "perdí 2 clientes" en lugar de "enfrenté desafíos".
- Si hay una "Ficha de voz" (de `linkedin-piloto`), respeta su vocabulario, su forma de tratar al lector (tú, vos, usted) y sus muletillas propias.

### Lo que NO se toca
- Los datos, números, nombres, historias y opiniones del usuario.
- Lo que el usuario escribió a propósito con su estilo (si usa un guion porque le gusta, pregunta).
- La extensión: no alargues. Si cambia, que sea para acortar.

## Entrega

1. El texto reescrito, completo, listo para copiar.
2. Una lista corta de los cambios principales (máximo 5 líneas: "saqué 3 guiones largos", "cambié 'potencia tu' por…").
3. Recomienda pasarlo por `linkedin-limpiador-invisible` y `linkedin-detector-ia`. Si hay herramienta de código, córrelos tú y muestra el resultado del detector.
