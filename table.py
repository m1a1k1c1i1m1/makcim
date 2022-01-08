from rich.console import Console
from rich.table import Table


def schow(name, count):
    table = Table(title="Star Wars Movies")

    table.add_column("Title", style="magenta")
    table.add_column("content", justify="right", style="green")

    table.add_row(f"{name[0]}", f"{count}")

    console = Console()
    console.print(table)
