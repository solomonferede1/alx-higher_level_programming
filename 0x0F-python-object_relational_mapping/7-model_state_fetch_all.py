#!/usr/bin/python3
"""
The 7-model_state_fetch_all

quering all the model state from the data base

"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def list_states():
    """ists all State objects from the database"""

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))


if __name__ == "__main__":
    list_states()
