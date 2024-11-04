Step 1: Set Up Your Project

1. Create a folder for your project (e.g., terminal-portfolio).


2. Install required libraries:

'''pip install rich inquirer'''



Step 2: Basic Portfolio Structure

We’ll structure the portfolio into sections like "About Me," "Skills," "Projects," and "Contact." Each section will be styled with the Rich library.

Here’s the starter code:
'''
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import inquirer

console = Console()

def display_header():
    console.print(Panel.fit("[bold blue]My Terminal Portfolio[/bold blue]", style="bold yellow"))

def about_me():
    console.print(Panel("[bold]About Me[/bold]\n"
                        "Hello! I'm [Your Name], a software developer specializing in Python.\n"
                        "I love creating innovative solutions and contributing to open-source projects.\n"
                        "Let's connect!", style="green"))

def skills():
    table = Table(title="Skills")
    table.add_column("Skill", justify="center", style="cyan", no_wrap=True)
    table.add_column("Level", justify="center", style="magenta")

    skills_list = [
        ("Python", "Advanced"),
        ("JavaScript", "Intermediate"),
        ("HTML/CSS", "Intermediate"),
        ("Git & GitHub", "Advanced"),
        ("SQL", "Intermediate")
    ]

    for skill, level in skills_list:
        table.add_row(skill, level)
    
    console.print(table)

def projects():
    table = Table(title="Projects")
    table.add_column("Project Name", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")

    project_list = [
        ("Portfolio Website", "A personal portfolio website to showcase my work."),
        ("Weather App", "A CLI app to get weather information."),
        ("Chatbot", "An AI chatbot built with Python and NLP techniques.")
    ]

    for name, desc in project_list:
        table.add_row(name, desc)

    console.print(table)

def contact_info():
    console.print(Panel("[bold]Contact Me[/bold]\n"
                        "Email: [your_email@example.com]\n"
                        "GitHub: [github.com/yourusername]\n"
                        "LinkedIn: [linkedin.com/in/yourusername]", style="green"))

def navigate():
    questions = [
        inquirer.List('section',
                      message="Which section would you like to view?",
                      choices=['About Me', 'Skills', 'Projects', 'Contact', 'Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['section']

def main():
    display_header()
    while True:
        section = navigate()
        
        console.clear()
        display_header()
        
        if section == 'About Me':
            about_me()
        elif section == 'Skills':
            skills()
        elif section == 'Projects':
            projects()
        elif section == 'Contact':
            contact_info()
        elif section == 'Exit':
            console.print("\n[bold]Thank you for visiting my portfolio![/bold] Goodbye!", style="yellow")
            break

        console.print("\nPress Enter to continue...")
        input()

if __name__ == "__main__":
    main()'''
