from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.sql.expression import and_, extract
from pprint import pprint

Base = declarative_base()

class Quote(Base):
    __tablename__ = "dow"
    id = Column(Integer, primary_key=True)
    quarter = Column(Integer)
    stock = Column(String)
    date = Column(Date)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Integer)
    percent_change = Column(Float)
    
engine = create_engine("sqlite:///../Resources/dow.sqlite")

conn = engine.connect()

session = Session(bind=engine)

# show the first 10
query = session.query(Quote).limit(10)
print(query)
for row in query:
    pprint(row.__dict__)
pprint([row.__dict__ for row in query.all()])
print(len(query.all()))

# find the min and max date
min_date, max_date = session.query(func.min(Quote.date), func.max(Quote.date)).first()
print(min_date, max_date)

# find the close average price
avg_close_price = session.query(func.avg(Quote.close_price)).first()[0]
print(avg_close_price)

# find average close price in February
avg_close_price_q = session.query(func.avg(Quote.close_price)).filter(
    and_(Quote.date > "2011-01-31", Quote.date < "2011-03-01")
)
avg_close_price = avg_close_price_q.first()[0]
print(avg_close_price_q)
print(avg_close_price)

# find average close price in February (another way)
avg_close_price_q = session.query(func.avg(Quote.close_price)).filter(
    extract("month", Quote.date) == "2"
)
avg_close_price = avg_close_price_q.first()[0]
print(avg_close_price_q)
print(avg_close_price)