"""
Inicialización de proyectos.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional


class ProjectInitializer:
    """Crea y configura nuevos proyectos de video."""
    
    def create_project(
        self,
        project_name: str,
        base_path: Optional[Path] = None,
    ) -> Path:
        """
        Crear estructura de directorios para un nuevo proyecto.
        
        Args:
            project_name: Nombre del proyecto
            base_path: Ruta base (default: ~/videos o cwd)
            
        Returns:
            Ruta absoluta del proyecto creado
        """
        # Determinar ruta base
        if base_path is None:
            base_path = Path.home() / "videos"
            base_path.mkdir(exist_ok=True)
        else:
            base_path = Path(base_path)
        
        project_path = base_path / project_name
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Crear estructura de directorios
        (project_path / "clips").mkdir(exist_ok=True)
        (project_path / "assets").mkdir(exist_ok=True)
        (project_path / "assets" / "sfx").mkdir(exist_ok=True)
        (project_path / "output").mkdir(exist_ok=True)
        (project_path / ".obs-ai").mkdir(exist_ok=True)
        
        # Crear configuración del proyecto
        config = {
            "name": project_name,
            "created": datetime.now().isoformat(),
            "settings": {
                "resolution": "1920x1080",
                "fps": 30,
                "audio_sample_rate": 48000,
                "transcription_language": "es",
            },
        }
        
        config_file = project_path / ".obs-ai" / "config.yaml"
        with open(config_file, "w", encoding="utf-8") as f:
            f.write(f"# Configuración del proyecto: {project_name}\n")
            f.write(f"name: {project_name}\n")
            f.write(f"created: {config['created']}\n")
        
        # Crear estado inicial
        state = {
            "project_name": project_name,
            "clips_recorded": 0,
            "last_modified": datetime.now().isoformat(),
        }
        
        state_file = project_path / ".obs-ai" / "state.json"
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
        
        # Crear DIRECTOR.md vacío (se llenará al editar)
        director_file = project_path / "DIRECTOR.md"
        with open(director_file, "w", encoding="utf-8") as f:
            f.write(f"# Proyecto: {project_name}\n\n")
            f.write("## Clips Disponibles\n\n")
            f.write("_Sin clips grabados aún._\n\n")
            f.write("## Instrucciones de Edición\n\n")
            f.write("_Pendiente de definir._\n")
        
        return project_path
