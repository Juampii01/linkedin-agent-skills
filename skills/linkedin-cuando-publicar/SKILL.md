---
name: linkedin-cuando-publicar
description: Arma el calendario de publicación de LinkedIn del usuario (qué día, a qué hora y con qué frecuencia) adaptado a su zona horaria y a la de su audiencia, y lo ajusta con sus propias métricas. Úsala cuando pregunte cuándo publicar, a qué hora, cuántas veces por semana o pida un calendario de LinkedIn.
---

# Cuándo publicar

No existe una hora mágica universal: depende de cuándo está conectada **tu** audiencia. Esta skill arranca con un punto de partida razonable y lo corrige con tus números.

## Preguntas (solo las que falten)

1. ¿En qué zona horaria vive tu audiencia principal? (puede no ser la tuya: si vendes a EE. UU. desde Argentina, manda la de ellos)
2. ¿Cuántas horas por semana puedes dedicarle a LinkedIn de verdad?
3. ¿Tienes estadísticas de posts anteriores? (impresiones y fecha/hora de cada post; se exportan desde "Analíticas" en LinkedIn)

## Punto de partida (sin datos)

Para audiencias profesionales B2B, en la zona horaria **de la audiencia**:
- Días: martes, miércoles y jueves primero; lunes y viernes después.
- Horarios a probar: antes de empezar a trabajar (7:30–9:00), mediodía (12:00–13:30) y salida (17:00–18:30).
- Fin de semana: solo si la audiencia son emprendedores o freelancers.

Dilo como lo que es: una hipótesis para probar, no una regla.

## Frecuencia según el tiempo disponible

| Tiempo por semana | Posts | Comentarios en posts ajenos | Respuestas |
|---|---|---|---|
| 1–2 h | 2 | 3 por día de publicación | todas, en la primera hora |
| 3–4 h | 3 | 5 por día | todas |
| 5 h o más | 4–5 | 5–10 por día | todas |

Consistencia > volumen: es mejor 2 posts todas las semanas que 5 una semana y 0 la siguiente.

## Calendario

Además del calendario, para cada semana entrega **las 10 personas con las que interactuar esa semana** (sacadas de la lista de `linkedin-con-quien-interactuar` si existe; si no, perfiles concretos a buscar), con una línea de por qué cada una.

Entrega una tabla de 2 semanas con: día · hora (en la zona del usuario **y** de la audiencia si difieren) · pilar · idea (de `linkedin-que-publicar` si hay banco) · bloque de 20 min para responder comentarios después de publicar.

## Ajuste con datos

Si el usuario pega sus estadísticas (o un CSV exportado):
1. Agrupa por día de la semana y franja horaria.
2. Calcula la mediana de impresiones y de interacciones de cada grupo (mediana, no promedio: un post viral distorsiona).
3. Muestra los 3 mejores huecos y los 2 peores.
4. Si hay menos de 10 posts, avisa que la muestra es chica y mantén la hipótesis general.

Si hay herramienta de código disponible, calcula con código en lugar de estimar.

## Recordatorios

Si el entorno permite tareas programadas, ofrece crear un recordatorio para cada publicación del calendario. Nunca publiques automáticamente: el recordatorio avisa, el usuario publica (o aprueba con `linkedin-piloto`).
