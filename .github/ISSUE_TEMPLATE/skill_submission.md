---
name: Skill Submission
about: Contribuir un nuevo skill de edición
title: '[SKILL] '
labels: skill, enhancement
assignees: ''
---

**Nombre del Skill**
Un nombre descriptivo para tu skill (ej. `background-blur`, `noise-remover`)

**Descripción**
¿Qué hace este skill? ¿Qué problema resuelve?

**Archivos incluidos**
- [ ] `SKILL.md` con instrucciones para el agente
- [ ] Script ejecutable (`.py`)
- [ ] `requirements.txt` (si tiene dependencias adicionales)
- [ ] Tests (opcional pero recomendado)
- [ ] Documentación de uso en `docs/skills/`

**Compatibilidad**
- [ ] Claude Code
- [ ] Codex
- [ ] Ollama (local)
- [ ] Otro: _____

**Dependencias adicionales**
Lista cualquier dependencia que no esté en `pyproject.toml`:
- `package-name>=version`

**Instrucciones de instalación**
```bash
# ¿Cómo se instala este skill?
cp -r skills/mi-skill ~/.config/obs-ai/skills/
```

**Ejemplo de uso**
```bash
obs-ai edit --skill mi-skill --option value
```

**Screenshots o demos**
Si aplica, agrega ejemplos de output o enlaces a demos.

**Checklist de contribución**
- [ ] El skill sigue la estructura definida en `docs/skills/creating-skills.md`
- [ ] El código está formateado con `black`
- [ ] El linting pasa con `ruff`
- [ ] La documentación es clara
- [ ] Licencia compatible (MIT recomendado)

**Información adicional**
Cualquier otra cosa que quieras compartir sobre tu skill.
