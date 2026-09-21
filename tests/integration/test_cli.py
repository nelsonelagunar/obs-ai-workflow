"""
Tests de integración para obs-ai-workflow.
"""

import pytest


class TestCLIIntegration:
    """Tests de integración para la CLI."""
    
    def test_cli_help(self):
        """Verificar que el CLI responde a --help."""
        import subprocess
        
        result = subprocess.run(
            ["python", "-m", "obs_ai.cli", "--help"],
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0
        assert "obs-ai" in result.stdout.lower()
        assert "init" in result.stdout.lower()
        assert "record" in result.stdout.lower()
