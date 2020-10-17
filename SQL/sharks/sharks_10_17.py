from shark_model import SharkAttack
from pprint import pprint
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.sql.expression import extract, and_ 

engine = create_engine(f"sqlite:///sharks.sqlite")
session = Session(bind = engine)

# results = session.query(SharkAttack).limit(10).all()
# for row in results:
#     pprint(row.__dict__)
    
    
    
# print all locations of shark attacks
location = session.query(SharkAttack.location)
# for l in location:
#     pprint(l)


# find the number of provoked attacks
provoked = session.query(func.count(SharkAttack.id)).filter(SharkAttack.type == "Provoked").first()[0]
print(f"The number of provoked attacks: {provoked}")
    
    
# # find the number of attacks in USA
usa = session.query(func.count(SharkAttack.id)).filter(SharkAttack.country == "USA").first()[0]
print(f"The number of attacks in USA: {usa}")

    
# # find the number of attacks in 2017
year2017 = session.query(func.count(SharkAttack.id)).filter(SharkAttack.year == "2017").first()[0]
print(f"The number of attacks in 2017: {year2017}")

# find the number of attacks while surfing
surfing = session.query(func.count(SharkAttack.id)).filter(SharkAttack.activity == "Surfing").first()[0]
print(f"The number of attacks while surfing: {surfing}")


# find the number of fatal attacks
fatal = session.query(func.count(SharkAttack.id)).filter(SharkAttack.fatal_y_n == "Y").first()[0]
print(f"The number of fatal attacks: {fatal}")
                        
                        
# find the number of fatal attacks while surfing
fatal_surfing = session.query(func.count(SharkAttack.id)).filter(and_(SharkAttack.fatal_y_n == "Y", SharkAttack.activity == "Surfing")).first()[0]
print(f"The number of fatal attacks while surfing: {fatal_surfing}")
                                                               
                                                               
# find the number of fatal attacks in Mozambique while spearfishing
Mozambique = session.query(func.count(SharkAttack.id)).filter(and_(SharkAttack.fatal_y_n == "Y", SharkAttack.country == "MOZAMBIQUE", SharkAttack.activity == "Spearfishing")).first()[0]
print(f"The number of fatal attacks in Mozambique while spearfishing: {Mozambique}")