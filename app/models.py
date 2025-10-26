from sqlalchemy import Column, Integer, String, Float
from app.db import Base

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    hour = Column(String, index=True)
    value = Column(Float)
