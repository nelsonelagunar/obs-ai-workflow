# obs-ai-workflow

**Automatiza tu workflow de edición de video con IA en Linux usando OBS Studio.**

Una herramienta open-source que replica funcionalidades de soluciones propietarias (VibeTube, Descript) pero nativa para Linux, con software libre y privacidad local-first.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange.svg)](https://github.com/nelsonelagunar/obs-ai-workflow/milestones)

---

## 🎯 ¿Qué hace?

```
┌─────────────────────────────────────────────────────────────────┐
│  1. GRABA   → Controla OBS Studio para capturar pantalla +     │
│               webcam en pistas separadas sincronizadas          │
│                                                                 │
│  2. TRANSCRIBE → Whisper AI genera subtítulos automáticos      │
│                  (español, inglés, +40 idiomas)                 │
│                                                                 │
│  3. EDITA   → Agente de IA (Claude/Codex/Ollama) selecciona    │
│               planos, corta, añade gráficos y subtítulos        │
│                                                                 │
│  4. EXPORTA → Genera versiones horizontal (1080p) y vertical   │
│               (9:16 para redes sociales)                        │
└─────────────────────────────────────────────────────────────────┘
```

**Resultado:** De grabación raw a video editado listo para publicar, sin tocar un editor de video.

---

## 🚀 Quickstart

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/nelsonelagunar/obs-ai-workflow.git
cd obs-ai-workflow

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -e .

# Verificar instalación
obs-ai --help
```

### Requisitos del sistema

```bash
# Ubuntu/Debian
sudo apt install obs-studio ffmpeg python3-pip

# Fedora
sudo dnf install obs-studio ffmpeg python3-pip

# Arch
sudo pacman -S obs-studio ffmpeg python-pip
```

### Primer workflow

```bash
# 1. Iniciar OBS (con WebSocket habilitado: Tools → WebSocket Server)
obs

# 2. Inicializar proyecto
obs-ai init mi-tutorial

# 3. Grabar clips
obs-ai record --start   # Inicia grabación
# ... haz tu demo ...
obs-ai record --stop    # Detiene grabación

# 4. Transcribir
obs-ai transcribe --all

# 5. Editar con IA
obs-ai edit --agent claude

# 6. Exportar
obs-ai export --format all
```

---

## 📖 Documentación

- [**Instalación**](docs/installation/) - Ubuntu, Fedora, Arch, Docker
- [**Uso**](docs/usage/) - Comandos, opciones, ejemplos
- [**Skills**](docs/skills/) - Crear y usar skills de edición
- [**Troubleshooting**](docs/troubleshooting.md) - Problemas comunes

---

## 🧩 Skills (Sistema de Extensiones)

Un **skill** es un módulo que enseña a la IA cómo realizar una tarea específica de edición.

### Skills incluidos

| Skill | Descripción |
|-------|-------------|
| `video-editor` | Edición multicam con selección automática de planos |
| `subtitle-burner` | Quema subtítulos con estilos personalizables |
| `vertical-crop` | Convierte video horizontal a 9:16 inteligente |
| `intro-outro` | Inserta intros y outros personalizados |

### Crear tu propio skill

```bash
# Estructura de skill
skills/
└── mi-skill/
    ├── SKILL.md           # Instrucciones para el agente
    ├── process.py         # Script ejecutable
    └── requirements.txt   # Dependencias específicas
```

Ver [**Guía de creación de skills**](docs/skills/creating-skills.md) para detalles.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Lee nuestra [**Guía de Contribución**](CONTRIBUTING.md) para empezar.

### Áreas donde necesitamos ayuda

- 📝 Documentación en más idiomas (PT, FR, DE)
- 🧪 Tests y CI/CD
- 🎨 Skills nuevos de la comunidad
- 🐛 Reporte de bugs y feedback

### Discusiones

- [GitHub Issues](https://github.com/nelsonelagunar/obs-ai-workflow/issues) - Bugs, features
- [GitHub Discussions](https://github.com/nelsonelagunar/obs-ai-workflow/discussions) - Questions, ideas, showcase

---

## 📋 Roadmap

| Versión | Estado | Features principales |
|---------|--------|---------------------|
| v0.1.0 | 🚧 Alpha | CLI básico, grabación, transcripción |
| v0.2.0 | 📋 Beta | Edición con IA, skills, export vertical |
| v0.3.0 | 📋 Release | Sistema de skills, paquetes PyPI/AUR |
| v1.0.0 | 📋 Estable | Docs completas, GUI opcional, Wayland full |

Ver [**Roadmap completo**](https://github.com/nelsonelagunar/obs-ai-workflow/milestones) para detalles.

---

## 🛠️ Stack Tecnológico

- **CLI:** Click + Rich (Python)
- **Grabación:** OBS Studio + obs-websocket
- **Procesamiento:** ffmpeg, PipeWire
- **Transcripción:** faster-whisper (CTranslate2)
- **IA:** Claude Code, Codex, Ollama (local)
- **Tests:** pytest, GitHub Actions

---

## 📄 Licencia

- **Código:** [MIT License](LICENSE)
- **Documentación:** CC BY-SA 4.0
- **Skills:** Cada skill mantiene su propia licencia (recomendado MIT)

---

## 🙏 Agradecimientos

Inspirado por proyectos como:
- [VibeTube](https://github.com/mutonby/vibetube) - La visión original (macOS)
- [OBS Studio](https://obsproject.com/) - Grabación open-source
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - Transcripción rápida
- [video-use](https://github.com/mutonby/vibetube/tree/main/video-use) - Skill de edición

---

## 📬 Contacto

- **Autor:** [@nelsonelagunar](https://github.com/nelsonelagunar)
- **Twitter:** [@9to9technews](https://twitter.com/9to9technews) (próximamente)
- **Sitio:** [9to9technews.mykeepper.app](https://9to9technews.mykeepper.app)

---

**Hecho con ❤️ para la comunidad Linux**
