"""
Configuración de pytest.
"""

import pytest
import sys
from pathlib import Path

# Agregar src al PATH para imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_project_dir(tmp_path):
    """Crear directorio de proyecto de ejemplo."""
    project_dir = tmp_path / "test-project"
    project_dir.mkdir()
    
    clips_dir = project_dir / "clips"
    clips_dir.mkdir()
    
    output_dir = project_dir / "output"
    output_dir.mkdir()
    
    return project_dir
