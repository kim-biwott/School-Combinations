from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    region = Column(String(100))
    county = Column(String(100))
    sub_county = Column(String(100))
    uic = Column(String(20))
    knec = Column(String(20))
    school_name = Column(String(200))
    cluster = Column(String(10))
    school_type = Column(String(50))
    disability_type = Column(String(50))
    accommodation_type = Column(String(50))
    gender = Column(String(20))

def create_session(engine=None):
    if engine is None:
        engine = create_engine('sqlite:///combinations.db')
    Session = sessionmaker(bind=engine)
    return Session()