#!/usr/bin/python3
"""
================================

the 9-model_state_filter_a module
prints the State object from the database that contains 'a'.
================================
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def fetch_first_state():
    """prints State object containing letter 'a'"""
    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id).all():
        if 'a' in instance.name:
            print("{}: {}".format(instance.id, instance.name))


if __name__ == "__main__":
    fetch_first_state()
