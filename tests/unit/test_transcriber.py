"""Tests para el servicio de transcripción."""

import pytest
from pathlib import Path


class TestWhisperTranscriber:
    """Tests para WhisperTranscriber."""
    
    def test_import(self):
        """Verificar que se puede importar WhisperTranscriber."""
        from obs_ai.services.transcriber import WhisperTranscriber
        assert WhisperTranscriber is not None
    
    def test_initialization(self):
        """Verificar inicialización básica."""
        from obs_ai.services.transcriber import WhisperTranscriber
        
        transcriber = WhisperTranscriber(
            model_size="tiny",
            language="es",
            device="cpu"
        )
        
        assert transcriber.model_size == "tiny"
        assert transcriber.language == "es"
        assert transcriber.device == "cpu"
        assert transcriber.model is None  # Lazy loading
    
    def test_format_time(self):
        """Verificar formato de tiempo SRT."""
        from obs_ai.services.transcriber import WhisperTranscriber
        
        transcriber = WhisperTranscriber()
        
        # Test casos
        assert transcriber._format_time(0.0) == "00:00:00,000"
        assert transcriber._format_time(1.5) == "00:00:01,500"
        assert transcriber._format_time(60.0) == "00:01:00,000"
        assert transcriber._format_time(3661.123) == "01:01:01,123"
