import pandas as pd
from sqlalchemy import create_engine
from models import School, Base, create_session
from rich.progress import track
from rich.console import Console
import os

console = Console()

def reset_database(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    console.print("Database tables recreated", style="bold green")

def seed_database(file_path):
    engine = create_engine('sqlite:///combinations.db')
    reset_database(engine)
    session = create_session(engine)
    try:
        df = pd.read_excel(file_path)
        console.print(f"Loaded {len(df)} records from spreadsheet", style="bold green")
        column_map = {
            "S/No.": "id",
            "REGION": "region",
            "COUNTY": "county",
            "SUB COUNTY": "sub_county",
            "UIC": "uic",
            "KNEC": "knec",
            "SCHOOL NAME": "school_name",
            "CLUSTER": "cluster",
            "TYPE": "school_type",
            "DISABILITY TYPE": "disability_type",
            "ACCOMODATION TYPE": "accommodation_type",
            "GENDER": "gender"
        }
        df = df.rename(columns=column_map)
        expected_columns = [
            "id", "region", "county", "sub_county", "uic", "knec",
            "school_name", "cluster", "school_type", "disability_type",
            "accommodation_type", "gender"
        ]
        df = df[[col for col in expected_columns if col in df.columns]]
        df = df[df['gender'].str.upper() != 'BOYS']
        df = df[df['accommodation_type'].str.upper() != 'DAY']
        def apply_uasingishu(row):
            if row['cluster'] in ['C3', 'C4']:
                return 'UASINGISHU'
            return row['school_name']
        if 'cluster' in df.columns and 'school_name' in df.columns:
            df['school_name'] = df.apply(apply_uasingishu, axis=1)
        records = df.to_dict(orient='records')
        for record in track(records, description="Seeding database..."):
            school = School(**record)
            session.add(school)
        session.commit()
        console.print(f"Inserted {len(records)} schools into database", style="bold green")
        count = session.query(School).count()
        console.print(f"Database now contains {count} schools", style="bold green")
    except Exception as e:
        session.rollback()
        console.print(f"Seeding failed: {str(e)}", style="bold red")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    excel_file = "senior-schools-in-kenya.xlsx"
    if not os.path.exists(excel_file):
        console.print(f"Error: Excel file '{excel_file}' not found", style="bold red")
        console.print("Please make sure the file exists in the same directory", style="bold yellow")
    else:
        seed_database(excel_file)