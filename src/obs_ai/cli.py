"""
CLI entry point for obs-ai-workflow.
"""

import click
from rich.console import Console
from rich.panel import Panel

from obs_ai import __version__

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="obs-ai")
def main():
    """
    obs-ai-workflow: Automated video editing for OBS Studio on Linux.
    
    Grabación, transcripción y edición de video con IA.
    """
    pass


@main.command()
@click.argument("project_name")
@click.option("--path", "-p", default=None, help="Ruta base para el proyecto")
def init(project_name, path):
    """
    Inicializar un nuevo proyecto de video.
    
    Ejemplo: obs-ai init mi-tutorial
    """
    from obs_ai.services.recorder import ProjectInitializer
    
    initializer = ProjectInitializer()
    project_path = initializer.create_project(project_name, base_path=path)
    
    console.print(Panel.fit(
        f"[green]✓[/green] Proyecto creado: [bold]{project_path}[/bold]\n\n"
        f"Siguientes pasos:\n"
        f"  1. Inicia OBS con WebSocket habilitado\n"
        f"  2. [bold]obs-ai record --start[/bold]\n"
        f"  3. Graba tu contenido\n"
        f"  4. [bold]obs-ai record --stop[/bold]",
        title="🎬 Proyecto inicializado",
        border_style="green",
    ))


@main.group()
def record():
    """
    Controlar grabación de OBS Studio.
    """
    pass


@record.command()
def start():
    """Iniciar grabación de un nuevo clip."""
    from obs_ai.services.recorder import OBSController
    
    controller = OBSController()
    
    try:
        controller.connect()
        clip_dir = controller.start_recording()
        console.print(Panel.fit(
            f"[red]🔴 Grabando[/red] clip: [bold]{clip_dir.name}[/bold]\n\n"
            f"Duración: [bold]0:00[/bold]\n"
            f"Presiona [bold]obs-ai record --stop[/bold] cuando termines.",
            title="Grabación en curso",
            border_style="red",
        ))
    except Exception as e:
        console.print(f"[red]✗ Error:[/red] {e}")
        raise SystemExit(1)
    finally:
        controller.disconnect()


@record.command()
def stop():
    """Detener grabación del clip actual."""
    from obs_ai.services.recorder import OBSController
    
    controller = OBSController()
    
    try:
        controller.connect()
        clip_info = controller.stop_recording()
        console.print(Panel.fit(
            f"[green]✓ Clip guardado[/green]\n\n"
            f"Archivos:\n"
            f"  - screen.webm ({clip_info['screen_size']})\n"
            f"  - webcam.webm ({clip_info['webcam_size']})\n"
            f"Duración: [bold]{clip_info['duration']}[/bold]",
            title="Grabación finalizada",
            border_style="green",
        ))
    except Exception as e:
        console.print(f"[red]✗ Error:[/red] {e}")
        raise SystemExit(1)
    finally:
        controller.disconnect()


@record.command()
def status():
    """Verificar estado de la grabación."""
    from obs_ai.services.recorder import OBSController
    
    controller = OBSController()
    
    try:
        controller.connect()
        is_recording = controller.get_recording_status()
        
        if is_recording:
            console.print("[red]🔴 OBS está grabando[/red]")
        else:
            console.print("[green]● OBS no está grabando[/green]")
    except Exception as e:
        console.print(f"[red]✗ Error:[/red] {e}")
        raise SystemExit(1)
    finally:
        controller.disconnect()


@main.command()
@click.option("--all", "all_clips", is_flag=True, help="Transcribir todos los clips")
@click.option("--clip", "-c", default=None, help="Transcribir clip específico")
@click.option("--language", "-l", default="es", help="Idioma para transcripción")
def transcribe(all_clips, clip, language):
    """
    Transcribir clips de video a subtítulos.
    """
    from obs_ai.services.transcriber import WhisperTranscriber
    
    transcriber = WhisperTranscriber(language=language)
    
    if all_clips:
        console.print("[bold]Transcribiendo todos los clips...[/bold]\n")
        # TODO: Implementar lógica para transcribir todos
    elif clip:
        console.print(f"[bold]Transcribiendo {clip}...[/bold]\n")
        # TODO: Implementar lógica para transcribir clip específico
    else:
        console.print("[yellow]Usa --all o --clip para especificar qué transcribir[/yellow]")


@main.command()
@click.option("--agent", "-a", default="claude", type=click.Choice(["claude", "codex", "ollama"]))
@click.option("--clip", "-c", default=None, help="Editar clip específico")
def edit(agent, clip):
    """
    Editar video con asistencia de IA.
    """
    from obs_ai.services.editor import AIVideoEditor
    
    editor = AIVideoEditor(agent=agent)
    
    console.print(f"[bold]Iniciando edición con {agent}...[/bold]\n")
    # TODO: Implementar lógica de edición


@main.command()
@click.option("--format", "-f", default="all", type=click.Choice(["horizontal", "vertical", "all"]))
@click.option("--resolution", "-r", default="1080p")
def export(format, resolution):
    """
    Exportar video final en diferentes formatos.
    """
    from obs_ai.services.exporter import VideoExporter
    
    exporter = VideoExporter()
    
    console.print(f"[bold]Exportando video en formato {format}...[/bold]\n")
    # TODO: Implementar lógica de exportación


@main.command()
def info():
    """Mostrar información del sistema y dependencias."""
    from obs_ai.utils.system import SystemInfo
    
    info = SystemInfo()
    
    console.print(Panel(
        f"[bold]obs-ai-workflow[/bold] v{__version__}\n\n"
        f"[bold]Python:[/bold] {info.python_version}\n"
        f"[bold]OBS Studio:[/bold] {info.obs_version}\n"
        f"[bold]ffmpeg:[/bold] {info.ffmpeg_version}\n"
        f"[bold]Sistema:[/bold] {info.os_name}",
        title="ℹ️ Información del sistema",
        border_style="blue",
    ))


if __name__ == "__main__":
    main()
