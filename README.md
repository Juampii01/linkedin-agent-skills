# Pack LinkedIn: 11 skills para Claude

Conecta Claude con tu LinkedIn y deja que te ayude con la cuenta entera: escribir posts, comentar, responder, optimizar tu perfil y decidir qué publicar, cuándo y con quién interactuar. Gratis.

**Vos tenés la última palabra:** ninguna skill publica, comenta ni envía nada sin tu aprobación.

## Las 11 skills

| Skill | Qué hace |
|---|---|
| `linkedin-ganchos-posts` | Escribe tu post completo usando 21 fórmulas de gancho probadas |
| `linkedin-comentarista` | Escribe comentarios de valor para posts de otras personas (y los publica si lo aprobás) |
| `linkedin-respuestas` | Responde los comentarios de tus posts y te marca a quién escribirle por privado |
| `linkedin-perfil` | Audita tu perfil en 10 puntos y te reescribe titular, "Acerca de", destacados y experiencia |
| `linkedin-que-publicar` | Arma tus 3 pilares de contenido y un banco de 30 ideas concretas |
| `linkedin-cuando-publicar` | Te dice qué días y a qué hora publicar, y lo ajusta con tus estadísticas |
| `linkedin-con-quien-interactuar` | Arma la lista de personas con las que tenés que interactuar y un plan diario de 15 minutos |
| `linkedin-humanizador` | Saca los guiones largos, las palabras típicas de IA y las estructuras repetidas |
| `linkedin-limpiador-invisible` | Borra los caracteres invisibles que quedan al copiar texto de herramientas de IA |
| `linkedin-detector-ia` | Pasa tu texto por 5 pruebas de "suena a IA" y te dice qué corregir |
| `linkedin-piloto` | Une todo: arma tu ficha de voz, se conecta a LinkedIn por el navegador y te lleva la rutina diaria y semanal |

## Instalación (5 minutos)

### En la app de Claude (web, escritorio o celular)

1. Activá la ejecución de código: **Settings → Capabilities → "Create and edit files"** (en planes Team o Enterprise lo habilita el admin).
2. Descargá el pack: botón verde **Code → Download ZIP** de este repositorio, o entrá a la carpeta [`dist/`](dist/) y bajá `pack-linkedin-11-skills.zip`.
3. Descomprimilo: adentro hay 11 archivos `.zip`, uno por skill. **No descomprimas esos 11**: se suben así.
4. En Claude andá a **Customize → Skills**, tocá **+** → **Create skill** → **Upload a skill** y subí cada `.zip`.
5. Asegurate de que las 11 estén activadas.

Las skills funcionan en todos los planes, incluido el gratis. [Guía oficial de Anthropic](https://support.claude.com/en/articles/12512180-usar-habilidades-en-claude)

### En Claude Code

Las skills que subiste en la app se sincronizan solas a Claude Code si iniciás sesión con la misma cuenta (comando `/skills` para verlas). O copialas a mano:

```bash
git clone https://github.com/Juampii01/linkedin-agent-skills
cp -r linkedin-agent-skills/skills/* ~/.claude/skills/
```

## Cómo empezar

1. Escribile a Claude: **"Usá linkedin-piloto y armemos mi ficha de voz"**. Te va a pedir unos textos tuyos para aprender cómo escribís.
2. Después: **"Optimizá mi perfil de LinkedIn"** (pegale el texto de tu perfil o el PDF que se descarga desde tu perfil con "Más → Guardar en PDF").
3. Y a publicar: **"Escribime un post sobre [tema]"**. Te da 3 ganchos, el post completo y lo pasa por el humanizador y el detector.

### Conectar con tu LinkedIn

Para que Claude lea tu feed, comente o responda en tu cuenta, necesita un navegador: **Claude in Chrome** (extensión) o el navegador integrado de la app de escritorio. Iniciás sesión en LinkedIn vos; Claude nunca te pide la contraseña. Sin navegador, todo funciona igual: Claude prepara y vos copiás y pegás.

## Avisos honestos

- **El detector usa 5 pruebas heurísticas**: busca los patrones que más delatan un texto generado. Ayuda mucho, pero ningún detector es infalible y no garantiza un resultado en herramientas externas.
- **El limpiador borra caracteres invisibles** (espacios de ancho cero, marcas de dirección, caracteres ocultos) que pueden quedar al copiar texto de IA, de documentos o de webs.
- **LinkedIn no permite la automatización masiva.** Las skills trabajan con aprobación y a ritmo humano (máximo 15 comentarios y 20 conexiones por día). No las uses para mandar mensajes en masa.

## Para desarrolladores

```bash
python tools/empaquetar.py   # valida las 11 skills y regenera dist/
```

Cada skill es una carpeta en `skills/` con su `SKILL.md`. El limpiador y el detector traen scripts en Python (solo librería estándar).
