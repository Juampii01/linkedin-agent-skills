---
name: linkedin-comentarista
description: Escribe comentarios de valor para los posts de otras personas en LinkedIn y, si el usuario lo aprueba, los publica con el navegador. Úsala cuando pida comentar posts, interactuar con su red, o preparar comentarios para su feed o para personas específicas.
---

# Comentar en posts de otras personas

Comentar bien en posts ajenos es la forma más rápida de que te vean personas que todavía no te siguen. Un buen comentario se lee como un mini post: aporta algo que el autor no dijo.

## Entrada

Una de estas:
- El texto de uno o varios posts (pegado por el usuario).
- Links a posts.
- "Comenta en mi feed": si hay navegador disponible (Claude in Chrome o el navegador integrado), abre LinkedIn en la sesión del usuario, lee los primeros 10 posts del feed y elige los 3–5 donde el usuario tiene algo útil que decir según su Ficha de voz y su tema.

Si hay una "Ficha de voz" (de `linkedin-piloto`), úsala para el tono y la experiencia del usuario.

## Cómo escribir cada comentario

Elige uno de estos 5 tipos según el post:

1. **Experiencia propia**: "Me pasó algo parecido con…, y lo que funcionó fue…"
2. **Dato o matiz**: agrega un número, una excepción o un caso donde la idea no aplica.
3. **Pregunta de seguimiento**: una pregunta concreta que el autor quiera responder (no "¿qué opinas?").
4. **Aplicación práctica**: "Para quien quiera aplicarlo mañana: 1) … 2) …"
5. **Desacuerdo respetuoso**: "Coincido en X, pero en Y lo vi distinto porque…"

Reglas:
- 2 a 5 líneas. Nunca más largo que el post.
- Prohibido: "¡Excelente post!", "Gran aporte", "Totalmente de acuerdo", "Gracias por compartir" como comentario completo.
- No menciones tu producto ni pongas links salvo que el usuario lo pida.
- Nada de emojis al inicio. Máximo 1.
- Nunca inventes experiencia del usuario. Si el tipo 1 requiere una historia que no conoces, usa otro tipo.
- Pasa cada comentario por las reglas de `linkedin-humanizador` antes de mostrarlo.

## Entrega

Para cada post:
- Autor y primera línea del post (para que el usuario sepa cuál es).
- El comentario propuesto y el tipo usado.
- Una alternativa más corta.

## Publicar (solo con aprobación)

Si el usuario quiere que los publiques y hay navegador disponible:
1. Muéstrale la lista final y espera un "sí" explícito **para cada comentario** (o "publica todos" explícito).
2. Publica de a uno, con al menos 1–2 minutos entre comentarios. Nunca más de 15 comentarios por día.
3. Después de publicar, confirma con el link del post.

Si no hay navegador, entrega los comentarios para copiar y pegar.

Advertencia que debes dar una vez, la primera vez que publiques por el usuario: LinkedIn no permite la automatización masiva; publicar pocos comentarios, revisados y espaciados, es lo seguro. La decisión final siempre es del usuario.
