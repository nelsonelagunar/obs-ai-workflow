# Guía de Contribución

¡Gracias por tu interés en contribuir a **obs-ai-workflow**! Este proyecto es una iniciativa comunitaria para democratizar la edición de video con IA en Linux.

## 🚀 Primeros Pasos

### 1. Fork y Clona

```bash
# Haz fork en GitHub y luego clona
git clone https://github.com/TU_USUARIO/obs-ai-workflow.git
cd obs-ai-workflow

# Agrega el repo original como upstream
git remote add upstream https://github.com/nelsonelagunar/obs-ai-workflow.git
```

### 2. Configura Entorno de Desarrollo

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar en modo desarrollo
pip install -e ".[dev]"

# Verificar instalación
obs-ai --help
```

### 3. Crea una Rama

```bash
# Para features
git checkout -b feature/nueva-feature

# Para fixes
git checkout -b fix/corregir-bug
```

## 📝 Tipos de Contribuciones

### 🐛 Reporte de Bugs

Usa la plantilla de [Bug Report](https://github.com/nelsonelagunar/obs-ai-workflow/issues/new?template=bug_report.md).

**Incluye:**
- Versión de `obs-ai` (`obs-ai --version`)
- Sistema operativo y versión
- Pasos para reproducir
- Comportamiento esperado vs. real
- Logs o screenshots si aplica

### 💡 Sugerencias de Features

Usa la plantilla de [Feature Request](https://github.com/nelsonelagunar/obs-ai-workflow/issues/new?template=feature_request.md).

**Incluye:**
- Descripción clara del feature
- Casos de uso
- Alternativas consideradas
- Contexto adicional

### 📖 Documentación

¡La documentación es crucial! Puedes ayudar con:

- Corregir errores tipográficos
- Mejorar claridad de explicaciones
- Traducir a otros idiomas (ES, PT, FR, DE)
- Agregar ejemplos de uso
- Crear tutoriales

### 🧪 Tests

Necesitamos más cobertura de tests:

```bash
# Correr tests existentes
pytest

# Agregar tests en tests/unit/ o tests/integration/
# Cada módulo debe tener su test correspondiente
```

### 🎨 Skills Nuevos

¿Creaste un skill de edición útil? [Lee la guía de creación de skills](docs/skills/creating-skills.md).

### 🔧 Código

**Estándares de código:**

```bash
# Formatear con black
black src/ tests/

# Lint con ruff
ruff check src/ tests/

# Asegurar imports ordenados
ruff check --select I src/ tests/
```

**Requisitos para PRs de código:**

- [ ] Tests para nueva funcionalidad
- [ ] Tests existentes pasan (`pytest`)
- [ ] Código formateado (`black`)
- [ ] Linting pasa (`ruff`)
- [ ] Documentación actualizada
- [ ] Descripción clara del cambio

## 🔄 Proceso de Pull Request

1. **Crea un issue** describiendo el cambio (a menos que sea un fix menor)
2. **Crea tu rama** desde `main`
3. **Haz commits** con mensajes descriptivos
4. **Push** a tu fork
5. **Abre el PR** en GitHub
6. **Espera revisión** - los mantenedores revisarán en 1-3 días
7. **Itera** según feedback
8. **Merge** - un mantenedor hará merge cuando esté listo

### Formato de Commits

```
feat: agregar transcripción batch
fix: corregir cálculo de offset de audio
docs: actualizar README con ejemplos
test: agregar tests para transcriber
refactor: simplificar lógica de exportación
```

## 📞 Comunicación

- **Issues**: Bugs, features, discusiones técnicas
- **Discussions**: Questions, ideas, showcase
- **Email**: nelson.e.laguna.r@gmail.com (para temas sensibles)

## 🎯 Áreas que Necesitan Ayuda

| Área | Dificultad | Descripción |
|------|------------|-------------|
| Tests | 🟢 Fácil | Agregar tests unitarios |
| Docs ES/PT | 🟢 Fácil | Traducir documentación |
| Skills | 🟡 Media | Crear skills de edición |
| Wayland | 🔴 Difícil | Soporte completo PipeWire |
| GUI | 🔴 Difícil | Interfaz gráfica opcional |

## 📜 Licencia

Al contribuir, aceptas que tu código sea licenciado bajo MIT License.

---

¡Gracias por hacer de `obs-ai-workflow` un proyecto mejor para todos! 🚀
