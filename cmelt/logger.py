import typer

from rich.console import Console

class Logger:
    
    def __init__(self):
        self.verbose: bool = False
        self.console = Console()
        self.error_console = Console(stderr=True)

    def debug(self, message: str) -> None:
        """Print a debug message if verbose mode is enabled."""
        if not self.verbose:
            return
        self.console.print(f'[dim][DEBUG][/dim] {message}')


    def info(self, message: str) -> None:
        """Print an informational message."""
        self.console.print(message)


    def warn(self, message: str) -> None:
        """Print a warning message."""
        self.console.print(f'[bold yellow]Warning:[/bold yellow] {message}')


    def error(self, message: str) -> None:
        """Print an error message."""
        self.error_console.print(f'[bold red]Error:[/bold red] {message}')


    def fatal(self, message: str, code: int = 1) -> None:
        """Print an error and exit with the given code."""
        self.error(message)
        raise typer.Exit(code)
    

log = Logger()
