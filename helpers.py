import csv
from datetime import datetime

def export_to_csv(schools):
    filename = f"filtered_schools_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'ID', 'Region', 'County', 'Sub County', 'UIC', 'KNEC', 
            'School Name', 'Cluster', 'Type', 'Disability Type', 
            'Accommodation', 'Gender'
        ])
        for school in schools:
            writer.writerow([
                school.id,
                school.region,
                school.county,
                school.sub_county,
                school.uic,
                school.knec,
                school.school_name,
                school.cluster,
                school.school_type,
                school.disability_type,
                school.accommodation_type,
                school.gender
            ])
    return filename

def get_input(prompt, default=""):
    value = input(f"{prompt} [{default}]: ") or default
    return value.strip()