from DB import Base
from sqlalchemy import String, Column, Integer, BigInteger, Date
from datetime import datetime


class Animal(Base):
    __tablename__ = 'animals base'

    id = Column(Integer, primary_key=True)                          # id породы
    type = Column(String)                                           # вид
    master = Column(String)                                         # хозяин
    birth_master = Column(String)                                   # хозяин при рождении
    name = Column(String)                                           # имя
    birthday = Column(Date, default=datetime.now().date())          # дата рождения
    STR = Column(Integer, default=0)                                # сила
    INT = Column(Integer, default=0)                                # интелект
    DEX = Column(Integer, default=0)                                # ловкость
    WIT = Column(Integer, default=0)                                # мудрость
    CON = Column(Integer, default=0)                                # выносливость
    MEN = Column(Integer, default=0)                                # духовность
    mother = Column(String)
    father = Column(String)
    children = Column(String)


class Fox(Animal):
    __tablename__ = 'fox type'




