#!/usr/bin/python3

"""
The model_city module

define the first city model
a python file that contains the class definition of a
City and an instance Base = declarative_base():

"""


from sqlalchemy import String, Integer, Column, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship
import sys


class City(Base):
    """"
    inherits from Base Tips
    id: that represents a column of an auto-generated,    unique integer,
    can’t be null and is a primary key
    name: that represents a column of a string with maximum 128 characters
    and can’t be null
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, nullable=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")


State.cities = relationship("City", cascade="all, delete, delete-orphan", back_populates="state")

