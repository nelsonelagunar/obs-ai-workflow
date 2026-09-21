"""
Información del sistema y verificación de dependencias.
"""

import subprocess
import shutil
from typing import Optional, Dict, Any


class SystemInfo:
    """Obtiene información del sistema y dependencias."""
    
    def __init__(self):
        self._obs_version: Optional[str] = None
        self._ffmpeg_version: Optional[str] = None
        self._python_version: str = self._get_python_version()
        self._os_name: str = self._get_os_name()
    
    def _get_python_version(self) -> str:
        """Obtener versión de Python."""
        import sys
        return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    
    def _get_os_name(self) -> str:
        """Obtener nombre del sistema operativo."""
        import platform
        return f"{platform.system()} {platform.release()}"
    
    @property
    def python_version(self) -> str:
        return self._python_version
    
    @property
    def os_name(self) -> str:
        return self._os_name
    
    @property
    def obs_version(self) -> str:
        if self._obs_version is None:
            self._obs_version = self._check_obs()
        return self._obs_version
    
    @property
    def ffmpeg_version(self) -> str:
        if self._ffmpeg_version is None:
            self._ffmpeg_version = self._check_ffmpeg()
        return self._ffmpeg_version
    
    def _check_obs(self) -> str:
        """Verificar instalación de OBS Studio."""
        obs_path = shutil.which("obs")
        if not obs_path:
            return "No encontrado (instala: sudo apt install obs-studio)"
        
        try:
            # OBS no tiene --version fácil, intentamos ejecutarlo
            result = subprocess.run(
                [obs_path, "--version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                return result.stdout.strip() or "Instalado"
        except Exception:
            pass
        
        return "Instalado (versión desconocida)"
    
    def _check_ffmpeg(self) -> str:
        """Verificar instalación de ffmpeg."""
        ffmpeg_path = shutil.which("ffmpeg")
        if not ffmpeg_path:
            return "No encontrado (instala: sudo apt install ffmpeg)"
        
        try:
            result = subprocess.run(
                [ffmpeg_path, "-version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                lines = result.stdout.split("\n")
                return lines[0].replace("ffmpeg version", "").strip() or "Instalado"
        except Exception:
            pass
        
        return "Instalado (versión desconocida)"
    
    def check_all(self) -> Dict[str, Any]:
        """Verificar todas las dependencias."""
        return {
            "python": self.python_version,
            "os": self.os_name,
            "obs": self.obs_version,
            "ffmpeg": self.ffmpeg_version,
        }
    
    def is_ready(self) -> bool:
        """Verificar si el sistema está listo para usar obs-ai."""
        checks = self.check_all()
        return "No encontrado" not in checks["obs"] and "No encontrado" not in checks["ffmpeg"]
