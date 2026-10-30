import typer
from rich.console import Console
from rich.panel import Panel
from .scorer import score_idea

app = typer.Typer()
console = Console()

def main(idea: str = typer.Argument(None)):
    if not idea:
        console.print('Usage: ideascore "An AI app to..."')
        return
    r = score_idea(idea)
    color = "green" if r.total >= 80 else "yellow"
    console.print(Panel(idea, title="💡 IDEA"))
    console.print(Panel(f"{r.total}/100 - {r.verdict}", title="📊 SCORE", border_style=color))
    for s in r.strengths: console.print(f"✅ {s}")
    for k in r.risks: console.print(f"⚠️ {k}")

if __name__ == "__main__":
    app()