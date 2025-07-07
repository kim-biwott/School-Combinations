from filter_logic import filter_schools
from display import display_title, display_results, display_menu
from helpers import export_to_csv, get_input
from models import create_session, School

def main():
    display_title()
    current_results = []
    while True:
        display_menu()
        choice = get_input("Choose an option", "1")
        if choice == "1":
            region = get_input("Enter region")
            county = get_input("Enter county")
            sub_county = get_input("Enter sub-county")
            cluster = get_input("Enter cluster (C1, C2, C3, C4)")
            gender = get_input("Enter gender (GIRLS, MIXED)")
            current_results = filter_schools(
                region=region or None,
                county=county or None,
                sub_county=sub_county or None,
                cluster=cluster or None,
                gender=gender or None
            )
            display_results(current_results)
        elif choice == "2":
            session = create_session()
            current_results = session.query(School).all()
            session.close()
            display_results(current_results)
        elif choice == "3":
            if not current_results:
                print("No results to export. Please run a filter first.")
                continue
            filename = export_to_csv(current_results)
            print(f"Results exported to {filename}")
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break

if __name__ == "__main__":
    main()