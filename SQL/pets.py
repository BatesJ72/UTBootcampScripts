from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declaritive_base
from sqlalchemy import Column, Integer, String

Base = decalarative_base()

class PetOwner(Base):
    __tablename__ = "pet_owner"
    pet_owner_id =  Column(Integer, primary_key = True)
    owner_name = Column(String(30))
    age = Column(Integer)
    pet_name = Column(String(30))
    pet_type = Column(String(30))
    phone = Column(String(30))
    
    engine = create_engine("postres://")