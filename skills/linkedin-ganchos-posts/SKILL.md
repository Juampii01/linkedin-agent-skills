---
name: linkedin-ganchos-posts
description: Escribe posts de LinkedIn completos usando 21 fórmulas de gancho probadas. Úsala cuando el usuario pida escribir, mejorar o reescribir un post de LinkedIn, o pida ganchos o primeras líneas para LinkedIn.
---

# Posts de LinkedIn con 21 fórmulas de gancho

En LinkedIn solo se ven las primeras 2–3 líneas antes del "…ver más". Si esas líneas no frenan el scroll, el resto del post no existe. Esta skill escribe el post entero, pero empieza por el gancho.

## Antes de escribir

Necesitas tres cosas. Si no están en la conversación, pregunta solo las que falten (en una sola pregunta):
1. **Tema o idea** (puede ser una nota suelta, una experiencia, un dato).
2. **Para quién es** (quién debería leerlo y qué quiere esa persona).
3. **Qué quieres que pase** después de leerlo: que comenten, que te escriban, que confíen en ti, que hagan clic.

Si hay una "Ficha de voz" (de la skill `linkedin-piloto`) en la conversación o en el proyecto, úsala. Si no, escribe en un tono directo y de primera persona.

## Las 21 fórmulas

Elige las 3 que mejor encajan con el tema y escribe un gancho con cada una. Cada gancho: máximo 2 líneas, menos de 210 caracteres en total.

| # | Fórmula | Ejemplo |
|---|---|---|
| 1 | **Resultado + tiempo** | "Pasé de 0 a 40 clientes en 6 meses sin pagar un solo anuncio." |
| 2 | **Error confesado** | "Perdí un cliente de 12.000 USD por un email de 3 líneas." |
| 3 | **Contra la creencia común** | "Publicar todos los días en LinkedIn me hizo perder seguidores." |
| 4 | **Antes / después** | "Hace un año contestaba emails a las 2 a. m. Hoy cierro la laptop a las 6." |
| 5 | **Número específico** | "Analicé 312 perfiles de LinkedIn. El 80 % comete el mismo error en la foto." |
| 6 | **Pregunta que duele** | "¿Cuántas horas por semana pierdes haciendo algo que podrías delegar?" |
| 7 | **Lista prometida** | "7 cosas que aprendí despidiendo a mi primer empleado:" |
| 8 | **Escena** (empieza en medio de la acción) | "Martes, 9:14. Mi socio me dice: 'creo que tenemos que cerrar'." |
| 9 | **Cita de alguien** | "'Tu producto es bueno, pero nadie sabe que existe.' Me lo dijo un inversor en 2019." |
| 10 | **Lo que nadie dice** | "Nadie te cuenta que el primer año como freelance ganas menos que en relación de dependencia." |
| 11 | **Dejé de hacer X** | "Dejé de hacer reuniones de una hora. Esto pasó con mi productividad:" |
| 12 | **Comparación inesperada** | "Contratar es como una cita: si en la primera ya dudas, no hay segunda." |
| 13 | **Dato + consecuencia** | "El 70 % de los compradores B2B ya decidió antes de hablar con ventas. Tu perfil es tu primer vendedor." |
| 14 | **Promesa concreta** | "Cómo escribir una propuesta que se lee en 2 minutos y se firma en 2 días." |
| 15 | **Opinión impopular** | "Opinión impopular: el 'networking' de eventos es la forma más cara de conseguir clientes." |
| 16 | **Detrás de escena** | "Así se ve por dentro un lanzamiento que facturó 30.000 USD (con los números)." |
| 17 | **Aprendizaje de un fracaso** | "Mi startup cerró. Lo único que haría distinto es esto:" |
| 18 | **Desafío al lector** | "Abre tu último post. Si la primera línea empieza con 'Hoy quiero hablar de', sigue leyendo." |
| 19 | **Pequeña historia con giro** | "Me rechazaron en 14 entrevistas. La 15 fue con la empresa que hoy es mi cliente." |
| 20 | **Plantilla / recurso** | "La plantilla que uso para responder a cualquier cliente enojado (cópiala):" |
| 21 | **Predicción** | "En 2 años, 'saber usar IA' va a estar en el CV igual que 'saber usar Excel'." |

Reglas para los ganchos:
- Específico gana a genérico: números, nombres, montos, días.
- Nada de "Hoy quiero hablar de…", "En el mundo actual…", "Les comparto…".
- La primera línea tiene que entenderse sola.
- No uses la fórmula si no tienes el dato real. **Nunca inventes números, clientes ni historias**: si la fórmula pide un dato que el usuario no dio, pídeselo o elige otra fórmula.

## Cuerpo del post

Después de que el usuario elija un gancho (o si pidió que elijas tú, elige el más fuerte y di por qué en una línea):

1. **Línea 2–3**: amplía la tensión del gancho, no la resuelvas todavía.
2. **Desarrollo**: una sola idea. Párrafos de 1–3 líneas. Una línea en blanco entre párrafos.
3. **Prueba**: el ejemplo, el número, la historia. Algo que solo el usuario podría escribir.
4. **Cierre**: una frase que resuma la idea en forma memorable.
5. **CTA** según el objetivo: una pregunta abierta (para comentarios), "escríbeme X por mensaje" (para leads) o nada (para autoridad).

Formato:
- 120 a 250 palabras salvo que pida otra cosa.
- Máximo 3 hashtags, al final, o ninguno.
- Emojis: 0 a 2. Nunca uno al inicio de cada línea.
- Sin enlaces externos en el cuerpo (LinkedIn reduce el alcance). Si hay link, sugerir ponerlo en el primer comentario.

## Entrega

Devuelve:
1. Los 3 ganchos, numerados, con el nombre de la fórmula.
2. El post completo con el gancho elegido, listo para copiar.
3. Una línea con el siguiente paso sugerido: pasarlo por `linkedin-humanizador` y `linkedin-detector-ia` antes de publicar.

Nunca publiques nada. El usuario siempre copia y publica él mismo, o lo publica `linkedin-piloto` con su aprobación explícita.
