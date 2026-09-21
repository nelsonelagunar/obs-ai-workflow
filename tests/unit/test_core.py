"""
Tests unitarios para obs-ai-workflow.
"""

import pytest
from pathlib import Path


class TestProjectInitializer:
    """Tests para ProjectInitializer."""
    
    def test_import(self):
        """Verificar que se puede importar ProjectInitializer."""
        from obs_ai.services.project_initializer import ProjectInitializer
        assert ProjectInitializer is not None
    
    def test_create_project_structure(self, tmp_path):
        """Verificar que crea la estructura básica de directorios."""
        from obs_ai.services.project_initializer import ProjectInitializer
        
        initializer = ProjectInitializer()
        project_path = initializer.create_project("test-project", base_path=tmp_path)
        
        assert project_path.exists()
        assert project_path.name == "test-project"
        assert (project_path / "clips").exists()
        assert (project_path / "output").exists()
        assert (project_path / ".obs-ai").exists()


class TestSystemInfo:
    """Tests para SystemInfo."""
    
    def test_import(self):
        """Verificar que se puede importar SystemInfo."""
        from obs_ai.utils.system import SystemInfo
        assert SystemInfo is not None
    
    def test_python_version(self):
        """Verificar que obtiene la versión de Python."""
        from obs_ai.utils.system import SystemInfo
        
        info = SystemInfo()
        assert info.python_version is not None
        assert "." in info.python_version
    
    def test_os_name(self):
        """Verificar que obtiene el nombre del OS."""
        from obs_ai.utils.system import SystemInfo
        
        info = SystemInfo()
        assert info.os_name is not None
        assert len(info.os_name) > 0


class TestCLI:
    """Tests para la CLI."""
    
    def test_import(self):
        """Verificar que se puede importar el CLI."""
        from obs_ai.cli import main
        assert main is not None
    
    def test_version(self):
        """Verificar que la versión está definida."""
        from obs_ai import __version__
        assert __version__ is not None
        assert "alpha" in __version__.lower() or "dev" in __version__.lower() or "." in __version__
