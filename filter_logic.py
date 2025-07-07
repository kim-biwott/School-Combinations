from models import create_session, School

def filter_schools(region=None, county=None, sub_county=None, cluster=None, gender=None):
    session = create_session()
    query = session.query(School)
    if region:
        query = query.filter(School.region.ilike(f"%{region}%"))
    if county:
        query = query.filter(School.county.ilike(f"%{county}%"))
    if sub_county:
        query = query.filter(School.sub_county.ilike(f"%{sub_county}%"))
    if cluster:
        query = query.filter(School.cluster.ilike(f"%{cluster}%"))
    if gender:
        query = query.filter(School.gender.ilike(f"%{gender}%"))
    query = query.filter(School.gender != 'BOYS')
    query = query.filter(School.accommodation_type != 'DAY')
    results = query.all()
    for school in results:
        if school.cluster in ['C3', 'C4']:
            school.school_name = 'UASINGISHU'
    session.close()
    return results