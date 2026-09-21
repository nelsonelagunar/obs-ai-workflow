---
name: video-editor
version: 1.0.0
description: Edición multicam automatizada con selección de planos basada en subtítulos
agent_compatible: [claude, codex, ollama]
---

# Video Editor Skill

## Objetivo

Editar video multicam alternando entre pantalla y webcam según el contenido hablado, generando un video final con subtítulos quemados.

## Inputs

- Proyecto con N clips en `clips/`
- Cada clip tiene:
  - `screen.webm` - Captura de pantalla (sin audio)
  - `webcam.webm` - Webcam + micrófono
  - `clip.srt` - Subtítulos generados
  - `metadata.json` - Duración, resolución, timestamp

## Output

- `output/final.mp4` (1920x1080, horizontal)
- `output/final.srt` (subtítulos consolidados)
- `output/metadata.json` (metadatos del video final)

## Instrucciones para el Agente

### 1. Análisis de Contenido

Lee todos los archivos `clip.srt` y clasifica cada segmento:

- **Demo UI**: Cuando el hablante describe interfaz, hace click, o muestra software
- **Diálogo directo**: Cuando el hablante mira a cámara, introduce temas, o concluye
- **Transición**: Silencios o cambios de tema

### 2. Generar EDL (Edit Decision List)

Crea un archivo JSON con la lista de cortes:

```json
{
  "shots": [
    {
      "clip": "clip_01",
      "source": "screen",
      "start": 0.0,
      "duration": 5.2,
      "transition": "fade",
      "transition_duration": 0.2
    },
    {
      "clip": "clip_01",
      "source": "webcam",
      "start": 5.2,
      "duration": 3.1,
      "transition": "fade",
      "transition_duration": 0.2
    }
  ]
}
```

### 3. Generar Comando ffmpeg

Usa `ffmpeg-python` o comandos directos para:

- Concatenar clips según EDL
- Alternar entre `screen.webm` y `webcam.webm`
- Insertar transiciones (fade in/out 200ms)
- Quemar subtítulos con fuente legible
- Normalizar audio (loudness EBU R128)

### 4. Ejecutar y Validar

```bash
python edit.py --project <path> --output <path>
```

Valida que:
- [ ] El video output existe y es reproducible
- [ ] Los subtítulos son legibles y están sincronizados
- [ ] Las transiciones son suaves
- [ ] El audio es consistente

## Comandos de ejemplo

```bash
# Ejecutar edición
python skills/video-editor/edit.py --project ~/videos/mi-tutorial --output output/final.mp4

# Con opciones avanzadas
python skills/video-editor/edit.py --project ~/videos/mi-tutorial --output output/final.mp4 --font "Arial" --font-size 24
```

## Dependencias

```
ffmpeg-python>=0.2.0
```

## Notas

- Mantener el audio original de `webcam.webm` como fuente única
- Los cortes deben ser en silencios o transiciones naturales
- Usar fuente sans-serif para subtítulos (Arial, Helvetica, Roboto)
- Color de subtítulos: blanco con borde negro para máximo contraste
