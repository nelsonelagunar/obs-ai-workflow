"""
Controlador de OBS Studio vía WebSocket.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

from obsws import obsws
from obsws.requests import StartRecord, StopRecord, GetRecordStatus


class OBSController:
    """Controla OBS Studio para grabación de clips multicam."""
    
    def __init__(
        self,
        host: str = "localhost",
        port: int = 4455,
        password: Optional[str] = None,
    ):
        self.host = host
        self.port = port
        self.password = password
        self.ws: Optional[obsws] = None
        self.current_clip: Optional[Dict[str, Any]] = None
        self.project_root: Optional[Path] = None
        
    def connect(self) -> None:
        """Conectar a OBS WebSocket."""
        try:
            self.ws = obsws(self.host, self.port, self.password)
            self.ws.connect()
        except Exception as e:
            raise ConnectionError(
                f"No se pudo conectar a OBS WebSocket en {self.host}:{self.port}. "
                f"Asegúrate de que OBS esté corriendo con WebSocket habilitado."
            ) from e
    
    def disconnect(self) -> None:
        """Desconectar de OBS WebSocket."""
        if self.ws:
            self.ws.disconnect()
            self.ws = None
    
    def get_recording_status(self) -> bool:
        """Verificar si OBS está grabando."""
        if not self.ws:
            raise RuntimeError("No conectado a OBS")
        
        response = self.ws.call(GetRecordStatus())
        return response.get("outputActive", False)
    
    def start_recording(self) -> Path:
        """Iniciar grabación de un nuevo clip."""
        if not self.ws:
            raise RuntimeError("No conectado a OBS")
        
        # Determinar directorio del proyecto (buscar .obs-ai o usar cwd)
        self.project_root = self._find_project_root()
        
        # Crear directorio para el clip
        clips_dir = self.project_root / "clips"
        clips_dir.mkdir(parents=True, exist_ok=True)
        
        clip_num = len(list(clips_dir.glob("clip_*"))) + 1
        clip_dir = clips_dir / f"clip_{clip_num:02d}"
        clip_dir.mkdir(exist_ok=True)
        
        # Iniciar grabación en OBS
        self.ws.call(StartRecord())
        
        # Guardar estado del clip
        self.current_clip = {
            "dir": clip_dir,
            "start_time": datetime.now(),
            "number": clip_num,
        }
        
        return clip_dir
    
    def stop_recording(self) -> Dict[str, Any]:
        """Detener grabación y guardar metadatos del clip."""
        if not self.ws or not self.current_clip:
            raise RuntimeError("No hay grabación activa")
        
        # Detener grabación en OBS
        self.ws.call(StopRecord())
        
        clip_dir = self.current_clip["dir"]
        end_time = datetime.now()
        duration = end_time - self.current_clip["start_time"]
        
        # OBS guarda el video en el directorio configurado
        # Necesitamos moverlo a nuestra estructura
        # (esto se implementará cuando tengamos la ruta de output de OBS)
        
        # Guardar metadatos
        metadata = {
            "clip_number": self.current_clip["number"],
            "start_time": self.current_clip["start_time"].isoformat(),
            "end_time": end_time.isoformat(),
            "duration_seconds": duration.total_seconds(),
            "screen_file": str(clip_dir / "screen.webm"),
            "webcam_file": str(clip_dir / "webcam.webm"),
            "sync_offset_ms": 0,  # Se calculará después
        }
        
        # Guardar metadata.json
        metadata_file = clip_dir / "metadata.json"
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        
        # Guardar sync.json (inicial)
        sync_file = clip_dir / "sync.json"
        with open(sync_file, "w", encoding="utf-8") as f:
            json.dump({"offset_ms": 0, "validated": False}, f, indent=2)
        
        result = {
            "clip_dir": str(clip_dir),
            "duration": str(duration).split(".")[0],  # Formato HH:MM:SS
            "screen_size": "pending",  # Se calculará después
            "webcam_size": "pending",
        }
        
        self.current_clip = None
        return result
    
    def _find_project_root(self) -> Path:
        """Buscar raíz del proyecto (directorio con .obs-ai/)."""
        current = Path.cwd()
        
        # Buscar hacia arriba
        for parent in [current] + list(current.parents):
            if (parent / ".obs-ai").exists():
                return parent
        
        # Si no encuentra, usar directorio actual
        return current
