from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from pprint import pprint


class SharkAttack(Base):
    __tablename__ = "sharks"
    id = Column(Integer, primary_key=True)
    case_number = Column(String)
    date = Column(String)
    year = Column(Integer)
    type = Column(String)
    country = Column(String)
    area = Column(String)
    location = Column(String)
    activity = Column(String)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    injury = Column(String)
    fatal_y_n = Column(String)
    time = Column(String)
    species = Column(String)
    investigator_or_source = Column(String)
    pdf = Column(String)
    original_order = Column(Integer)
    
engine = create_engine(f"sqlite:///sharks.sqlite")
# pprint(engine.execute("SELECT * FROM sharks LIMIT 10").fetchall())

