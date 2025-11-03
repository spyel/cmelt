import os
import logging
from typing import Optional

import typer

app = typer.Typer()


@app.command()
def build(
    ctx: typer.Context,
    project: Optional[str] = typer.Argument(None, help='Name of the project to build. If omitted, builds all projects.'),
    clean: bool = typer.Option(False, '--clean', '-c', help='Remove build artifacts before building.'),
    force: bool = typer.Option(False, '--force', '-f', help='Rebuild all targets regardless of state.')
) -> None:
    """Build one or more C/C++ projects defined in the configuration file."""
    logging.info('🚧 The "build" command is not implemented yet.')


@app.command()
def clean(
    ctx: typer.Context,
    project: Optional[str] = typer.Argument(None, help='Project name to clean. If omitted, cleans all projects.')
) -> None:
    """Clean build artifacts for one or more projects."""
    logging.info('🚧 The "clean" command is not implemented yet.')


@app.callback()
def main(
    ctx: typer.Context,
    filepath: str = typer.Option('build.toml', '--file', '-f', help='Path to the build configuration file.'),
    directory: str = typer.Option(None, '--dir', '-C', help='Change to this directory before loading configuration.'),
    verbose: bool = typer.Option(False, '--verbose', '-v', help='Enable verbose logging output.')
) -> None:
    """CMelt – A build system for C/C++ projects."""
    if directory:
        os.chdir(directory)
    ctx.obj = {'filepath': filepath}
