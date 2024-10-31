"""Console script for sl_common."""
import sl_common

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for sl_common."""
    console.print("Replace this message by putting your code into "
               "sl_common.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
