#!/usr/bin/python3
"""
================================

8-model_state_fetch_first module
prints the first State object from the database given as command argument.
================================
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def fetch_first_state():
    """prints the first State object from the database"""
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).order_by(State.id).first()
    if (instance):
        print("{}: {}".format(instance.id, instance.name))
    else:
        print()


if __name__ == "__main__":
    fetch_first_state()
