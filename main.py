import inquirer
from rich.console import Console
from rich.table import Table

console = Console()

def show_about_me():
    console.print("[bold blue]About Me[/bold blue]", style="bold underline")
    console.print(
        "Hello! I am Danish Veer Rana, a passionate programmer and student with expertise in Python, "
        "voice and gesture control projects, and a love for creating impactful tools. "
        "This portfolio showcases my journey, skills, and projects."
    )

def show_skills():
    console.print("[bold blue]Skills[/bold blue]", style="bold underline")
    table = Table(title="Skills", style="cyan")
    table.add_column("Category", style="magenta", justify="left")
    table.add_column("Details", style="green", justify="left")
    table.add_row("Programming", "Python, JavaScript, C++")
    table.add_row("Technologies", "Voice & Gesture Control, Text-to-Speech")
    table.add_row("Other", "Editing, Photography")
    console.print(table)

def show_projects():
    console.print("[bold blue]Projects[/bold blue]", style="bold underline")
    console.print(
        "[green]1. VYOM:[/green] A voice and gesture control system designed for low-memory devices.\n"
        "[green]2. VCG:[/green] A voice-controlled graphics application.\n"
        "[green]3. CodePen PCM Projects:[/green] Visual tools for learning physics, chemistry, and mathematics."
    )

def show_contact():
    console.print("[bold blue]Contact[/bold blue]", style="bold underline")
    console.print(
        "Email: danishveer@example.com\n"
        "GitHub: [link=https://github.com/danishveer]github.com/danishveer[/link]\n"
        "LinkedIn: [link=https://linkedin.com/in/danishveer]linkedin.com/in/danishveer[/link]"
    )

def main_menu():
    while True:
        questions = [
            inquirer.List(
                "menu",
                message="Select a section to explore:",
                choices=["About Me", "Skills", "Projects", "Contact", "Exit"],
            )
        ]
        answers = inquirer.prompt(questions)

        if answers["menu"] == "About Me":
            show_about_me()
        elif answers["menu"] == "Skills":
            show_skills()
        elif answers["menu"] == "Projects":
            show_projects()
        elif answers["menu"] == "Contact":
            show_contact()
        elif answers["menu"] == "Exit":
            console.print("[bold red]Thank you for exploring my terminal portfolio![/bold red]")
            break

if __name__ == "__main__":
    console.print("[bold green]Welcome to My Terminal Portfolio![/bold green]\n", style="bold")
    main_menu()
