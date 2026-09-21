# Instalación en Ubuntu/Debian

## Requisitos previos

- Ubuntu 22.04+ o Debian 12+
- Python 3.10+
- 2GB de espacio en disco (mínimo)
- 4GB RAM recomendado

## Paso 1: Instalar dependencias del sistema

```bash
# Actualizar repositorios
sudo apt update

# Instalar OBS Studio
sudo apt install -y obs-studio

# Instalar ffmpeg
sudo apt install -y ffmpeg

# Instalar Python y pip (si no están)
sudo apt install -y python3 python3-pip python3-venv

# Instalar PipeWire (para Wayland)
sudo apt install -y pipewire wireplumber
```

## Paso 2: Configurar OBS WebSocket

OBS Studio 28+ incluye WebSocket por defecto.

1. Abre OBS Studio
2. Ve a **Tools → WebSocket Server Settings**
3. Configura:
   - ✅ Enable WebSocket server
   - Server Port: `4455`
   - Authentication: ✅ Required
   - Password: `tu_password_seguro`
4. Click en **Apply** y **OK**

## Paso 3: Instalar obs-ai-workflow

```bash
# Clonar repositorio
git clone https://github.com/nelsonelagunar/obs-ai-workflow.git
cd obs-ai-workflow

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar en modo desarrollo
pip install -e .

# Verificar instalación
obs-ai --help
```

## Paso 4 (Opcional): Aceleración GPU NVIDIA

Si tienes GPU NVIDIA:

```bash
# Instalar dependencias CUDA
pip install -e ".[gpu]"

# Configurar variables de entorno
export LD_LIBRARY_PATH=$(python3 -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))')
```

## Paso 5: Verificar instalación

```bash
# Verificar sistema
obs-ai info

# Deberías ver algo como:
# ℹ️ Información del sistema
# ─────────────────────────────
# obs-ai-workflow v0.1.0-alpha
# Python: 3.11.5
# OBS Studio: 30.0.2
# ffmpeg: 6.0
# Sistema: Linux 6.5.0
```

## Solución de problemas

### OBS no aparece en PATH

```bash
# Verificar instalación
which obs

# Si no aparece, reinstalar
sudo apt install --reinstall obs-studio
```

### Error de permisos en Wayland

Si usas Wayland y OBS no puede capturar pantalla:

```bash
# Instalar portal de escritorio
sudo apt install -y xdg-desktop-portal xdg-desktop-portal-gtk

# Reiniciar sesión
```

### WebSocket no conecta

- Verifica que OBS esté corriendo
- Verifica que WebSocket esté habilitado (Tools → WebSocket Server Settings)
- Verifica puerto y contraseña en tu configuración

---

[Siguiente: Primer proyecto](../usage/first-project.md)
