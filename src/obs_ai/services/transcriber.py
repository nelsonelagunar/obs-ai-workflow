"""
Servicios de transcripción con Whisper.
"""

from pathlib import Path
from typing import Optional, List, Dict, Any

from faster_whisper import WhisperModel


class WhisperTranscriber:
    """Transcribe audio de clips usando faster-whisper."""
    
    def __init__(
        self,
        model_size: str = "medium",
        language: str = "es",
        device: str = "cpu",
    ):
        self.model_size = model_size
        self.language = language
        self.device = device
        self.model: Optional[WhisperModel] = None
        
    def _load_model(self) -> None:
        """Cargar modelo Whisper (lazy loading)."""
        if self.model is None:
            compute_type = "float16" if self.device == "cuda" else "int8"
            self.model = WhisperModel(
                self.model_size,
                device=self.device,
                compute_type=compute_type,
            )
    
    def transcribe_clip(
        self,
        clip_dir: Path,
        output_dir: Optional[Path] = None,
    ) -> Dict[str, Any]:
        """
        Transcribir un clip de video.
        
        Args:
            clip_dir: Directorio del clip con webcam.webm
            output_dir: Directorio de output (default: clip_dir)
            
        Returns:
            Información de la transcripción
        """
        self._load_model()
        
        clip_path = Path(clip_dir)
        audio_file = clip_path / "webcam.webm"
        
        if not audio_file.exists():
            raise FileNotFoundError(f"No se encontró {audio_file}")
        
        # Transcribir
        segments, info = self.model.transcribe(
            str(audio_file),
            language=self.language if self.language != "auto" else None,
        )
        
        # Generar SRT
        output_path = output_dir or clip_path
        srt_file = output_path / "clip.srt"
        
        segment_list = list(segments)
        self._write_srt(segment_list, srt_file)
        
        return {
            "clip_dir": str(clip_path),
            "language": info.language,
            "language_probability": info.language_probability,
            "duration": info.duration,
            "segments_count": len(segment_list),
            "srt_file": str(srt_file),
        }
    
    def _write_srt(self, segments: List, output_file: Path) -> None:
        """Escribir segmentos a archivo SRT."""
        with open(output_file, "w", encoding="utf-8") as f:
            for i, segment in enumerate(segments, 1):
                start = segment.start
                end = segment.end
                text = segment.text.strip()
                
                f.write(f"{i}\n")
                f.write(f"{self._format_time(start)} --> {self._format_time(end)}\n")
                f.write(f"{text}\n\n")
    
    def _format_time(self, seconds: float) -> str:
        """Convertir segundos a formato SRT (HH:MM:SS,mmm)."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
    
    def transcribe_all(self, project_dir: Path) -> List[Dict[str, Any]]:
        """Transcribir todos los clips de un proyecto."""
        project_path = Path(project_dir)
        clips_dir = project_path / "clips"
        
        if not clips_dir.exists():
            raise FileNotFoundError(f"No se encontró {clips_dir}")
        
        results = []
        clip_dirs = sorted(clips_dir.glob("clip_*"))
        
        for clip_dir in clip_dirs:
            print(f"Transcribiendo {clip_dir.name}...")
            try:
                result = self.transcribe_clip(clip_dir)
                results.append(result)
                print(f"  ✓ {result['segments_count']} segmentos")
            except Exception as e:
                print(f"  ✗ Error: {e}")
                results.append({
                    "clip_dir": str(clip_dir),
                    "error": str(e),
                })
        
        return results
