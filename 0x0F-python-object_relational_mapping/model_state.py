#!/usr/bin/python3

"""
The model state module

define the first stae model
a python file that contains the class definition of a
State and an instance Base = declarative_base():

"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column
import sys


Base = declarative_base()


class State(Base):
    """"
    inherits from Base Tips
    id: that represents a column of an auto-generated,    unique integer,
    can’t be null and is a primary key
    name: that represents a column of a string with maximum 128 characters
    and can’t be null
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
