#!/usr/bin/python3
"""
================================
11-medel_state_insert module
Add a new state to the database
================================
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def add_state():
    """prints the first State object from the database"""
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    new_state = session.query(State).filter(State.name == "Louisiana").first()
    print(new_state.id)


if __name__ == "__main__":
    add_state()
