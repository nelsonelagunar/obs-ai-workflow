# Ejemplo básico de workflow

#!/bin/bash
# Este script demuestra el workflow completo de obs-ai-workflow

set -e

echo "🎬 obs-ai-workflow - Demo de workflow básico"
echo "=============================================="
echo

# 1. Inicializar proyecto
echo "1️⃣  Inicializando proyecto..."
obs-ai init "mi-primer-tutorial"
echo

# 2. Verificar estado del sistema
echo "2️⃣  Verificando sistema..."
obs-ai info
echo

# 3. Instrucciones para el usuario
echo "3️⃣  Siguientes pasos:"
echo
echo "   a) Abre OBS Studio:"
echo "      obs"
echo
echo "   b) Habilita WebSocket (si es la primera vez):"
echo "      Tools → WebSocket Server Settings"
echo "      - Enable: ✓"
echo "      - Port: 4455"
echo "      - Password: tu_password"
echo
echo "   c) Inicia grabación:"
echo "      obs-ai record --start"
echo
echo "   d) Graba tu contenido..."
echo
echo "   e) Detén grabación:"
echo "      obs-ai record --stop"
echo
echo "   f) Transcribe:"
echo "      obs-ai transcribe --all"
echo
echo "   g) Edita con IA:"
echo "      obs-ai edit --agent claude"
echo
echo "   h) Exporta:"
echo "      obs-ai export --format all"
echo
echo "=============================================="
echo "¡Listo! Tu video estará en output/final.mp4"
