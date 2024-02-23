from DB import Base
from sqlalchemy import String, Column, Integer, BigInteger


class Animal(Base):
    __tablename__ = 'animals base'

    id = Column(Integer, primary_key=True)
    name = Column(String)
