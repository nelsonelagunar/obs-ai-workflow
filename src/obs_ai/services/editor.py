"""
Servicios de edición de video con IA.
"""

from pathlib import Path
from typing import Optional, Dict, Any


class AIVideoEditor:
    """Editor de video asistido por IA (Claude Code, Codex, Ollama)."""
    
    def __init__(self, agent: str = "claude"):
        self.agent = agent
        
    def prepare_context(self, project_dir: Path) -> Path:
        """
        Preparar contexto (DIRECTOR.md) para el agente de IA.
        
        Args:
            project_dir: Directorio del proyecto
            
        Returns:
            Ruta al DIRECTOR.md generado
        """
        project_path = Path(project_dir)
        
        # Recopilar información de clips
        clips_info = []
        clips_dir = project_path / "clips"
        
        if clips_dir.exists():
            for clip_dir in sorted(clips_dir.glob("clip_*")):
                metadata_file = clip_dir / "metadata.json"
                srt_file = clip_dir / "clip.srt"
                
                clip_data = {
                    "dir": clip_dir.name,
                    "metadata": None,
                    "subtitles": None,
                }
                
                if metadata_file.exists():
                    import json
                    with open(metadata_file) as f:
                        clip_data["metadata"] = json.load(f)
                
                if srt_file.exists():
                    clip_data["subtitles"] = srt_file.read_text()
                
                clips_info.append(clip_data)
        
        # Generar DIRECTOR.md
        director_content = self._generate_director_md(project_path.name, clips_info)
        director_file = project_path / "DIRECTOR.md"
        director_file.write_text(director_content, encoding="utf-8")
        
        return director_file
    
    def _generate_director_md(self, project_name: str, clips_info: list) -> str:
        """Generar contenido de DIRECTOR.md."""
        content = f"""# Proyecto: {project_name}

## Clips Disponibles

"""
        for clip in clips_info:
            duration = "N/A"
            if clip["metadata"] and "duration_seconds" in clip["metadata"]:
                duration = f"{clip['metadata']['duration_seconds']:.1f}s"
            
            content += f"- **{clip['dir']}**: {duration}\n"
        
        content += """
## Instrucciones de Edición

1. **Análisis de contenido:**
   - Revisa los subtítulos de cada clip
   - Identifica momentos de demo de UI → usar pantalla
   - Identifica diálogo directo → usar webcam
   - Marca transiciones naturales en silencios

2. **Selección de planos:**
   - Alterna entre pantalla y webcam según el contexto
   - Usa PiP cuando se explique algo sobre la UI
   - Mantén webcam en introducciones y conclusiones

3. **Edición:**
   - Inserta transiciones suaves (fade 200ms)
   - Quema subtítulos con fuente legible
   - Ajusta niveles de audio

4. **Exportación:**
   - `output/final.mp4` (1920x1080, horizontal)
   - `output/final_9x16.mp4` (1080x1920, vertical)
   - `output/final.srt` (subtítulos consolidados)

## Assets Opcionales

- Intro: `assets/intro.mp4`
- Outro: `assets/outro.mp4`
- SFX: `assets/sfx/`

## Notas

Este archivo será leído por un agente de IA (Claude Code, Codex, o Ollama)
que ejecutará los comandos de edición necesarios usando ffmpeg y Python.
"""
        return content
    
    def run_agent(self, project_dir: Path, instructions: Optional[str] = None) -> Dict[str, Any]:
        """
        Ejecutar agente de IA para editar el video.
        
        Args:
            project_dir: Directorio del proyecto
            instructions: Instrucciones adicionales (opcional)
            
        Returns:
            Resultado de la edición
        """
        # Preparar contexto
        director_file = self.prepare_context(project_dir)
        
        # Aquí se implementará la ejecución del agente
        # Por ahora, retornamos un placeholder
        return {
            "status": "pending",
            "message": "La ejecución de agentes de IA se implementará en la próxima iteración",
            "director_file": str(director_file),
            "agent": self.agent,
        }
