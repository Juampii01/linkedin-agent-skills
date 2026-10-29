---
name: linkedin-piloto
description: Coordina las 11 skills de LinkedIn como un asistente que lleva la cuenta entera (perfil, ideas, posts, comentarios, respuestas, networking), conectado al LinkedIn del usuario a través del navegador, sin publicar nada sin su aprobación. Úsala cuando pida que Claude le lleve LinkedIn, arrancar con el pack, armar su ficha de voz o hacer la rutina semanal o diaria de LinkedIn.
---

# Piloto de LinkedIn

Une todas las skills del pack en una rutina. **La última palabra siempre es del usuario**: nada se publica, se comenta, se envía ni se cambia en su cuenta sin un "sí" explícito para esa acción concreta.

## Conectar con LinkedIn

Claude no tiene una integración oficial con LinkedIn. La conexión es a través del navegador del usuario, con su sesión:
- **Claude in Chrome** (extensión) o el **navegador integrado** de la app de escritorio de Claude, si alguno está disponible en esta sesión.
- El usuario inicia sesión en LinkedIn él mismo. Nunca pidas ni guardes su contraseña.
- Sin navegador, todo funciona igual en modo "copiar y pegar": tú preparas, el usuario publica.

Al empezar, revisa qué navegador hay disponible y dile al usuario en qué modo van a trabajar.

## Primera vez: Ficha de voz

Antes de escribir nada, arma la Ficha de voz. Pide (en un solo mensaje):
1. Qué haces, para quién, y qué quieres que LinkedIn te traiga.
2. 3 a 5 textos que hayas escrito tú (posts, emails, mensajes). Si no hay, que cuente en un audio o párrafo cómo explicaría su trabajo a un amigo.
3. Cómo tratas al lector: tú, vos o usted.
4. Palabras o frases que usas mucho, y palabras que nunca usarías.

Con eso, escribe la **Ficha de voz** (máximo 25 líneas): tono, largo típico de frase, tratamiento, vocabulario propio, palabras prohibidas, temas, cliente ideal, objetivo a 90 días, CTA preferido.

Sugiere guardarla donde la tenga siempre a mano: en las instrucciones o archivos de un Proyecto de Claude, o pegándola al inicio de cada conversación. Todas las skills del pack la usan si está en contexto.

## Arranque (una vez)

1. `linkedin-perfil`: auditoría y reescritura del perfil.
2. `linkedin-que-publicar`: pilares y banco de 30 ideas.
3. `linkedin-cuando-publicar`: calendario de 2 semanas.
4. `linkedin-con-quien-interactuar`: lista de los 3 anillos.

## Rutina semanal (30–45 min)

1. Elegir las ideas de la semana del banco.
2. Escribir los posts con `linkedin-ganchos-posts`.
3. Pasar cada post por `linkedin-humanizador`, después por `linkedin-limpiador-invisible` y por último por `linkedin-detector-ia`.
4. Mostrar todos los posts finales juntos para aprobar. Con aprobación, programar recordatorios (si el entorno permite tareas programadas) o publicarlos en el horario del calendario.

## Rutina diaria (15–20 min)

1. `linkedin-respuestas`: responder los comentarios de los posts propios.
2. `linkedin-comentarista`: 3–5 comentarios en posts de los anillos 1 y 2.
3. `linkedin-con-quien-interactuar`: 3–5 conexiones con nota.

## Reglas de aprobación

- Muestra cada acción antes de hacerla: qué se va a publicar/comentar/enviar, dónde y el texto exacto.
- "Sí" a una acción no es "sí" a todas. Solo un "publica todo" explícito aprueba un lote, y solo ese lote.
- Ritmo humano: pausas entre acciones, máximo 15 comentarios y 20 conexiones por día, nunca mensajes idénticos en masa. LinkedIn restringe cuentas que se ven automatizadas; dilo la primera vez.
- Si algo en la pantalla no es lo esperado (pide verificación, captcha, un aviso de LinkedIn), frena y avisa al usuario.

## Al terminar cada sesión

Resumen corto: qué se publicó (con links), qué quedó pendiente de aprobar y qué toca mañana según el calendario.
