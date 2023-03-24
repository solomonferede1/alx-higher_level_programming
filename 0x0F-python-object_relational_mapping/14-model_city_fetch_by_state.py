#!/usr/bin/python3

"""
===================================
14-model_city_fetch_by_state module

fetches all the city of the state
==================================
"""


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def all_cities():
    """print all city"""
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).all():
        for city in state.cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    all_cities()
