from rich.console import Console
from rich.table import Table

console = Console()

def display_title():
    title = "SCHOOL FILTERING APPLICATION"
    console.print(f"\n[bold blue]{title}[/bold blue]", justify="center")
    console.print("[bold green]Filter Schools by Region, County, Sub-County, Cluster and Gender[/bold green]\n", justify="center")

def display_results(schools):
    if not schools:
        console.print("No schools found matching the criteria", style="bold yellow")
        return
    table = Table(title=f"Filtered Schools ({len(schools)} found)", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="cyan")
    table.add_column("Region")
    table.add_column("County")
    table.add_column("Sub County")
    table.add_column("School Name")
    table.add_column("Cluster")
    table.add_column("Accom.")
    table.add_column("Gender")
    for school in schools:
        table.add_row(
            str(school.id),
            school.region,
            school.county,
            school.sub_county,
            school.school_name,
            school.cluster,
            school.accommodation_type,
            school.gender
        )
    console.print(table)

def display_menu():
    console.print("\n[bold cyan]Main Menu[/bold cyan]")
    console.print("1. Filter Schools")
    console.print("2. List All Schools")
    console.print("3. Export Results")
    console.print("4. Exit")