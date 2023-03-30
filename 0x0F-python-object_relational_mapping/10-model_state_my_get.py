#!/usr/bin/python3
"""
================================

10-model_state_my_get module
prints the State object with the name passed as argument from the database
================================
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def search_state_by_name():
    """prints the first State object from the database"""
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State.id).filter(State.name == (sys.argv[4], )).first()
    if res is not None:
        print(res[0])
    else:
        print("Not found")


if __name__ == "__main__":
    search_state_by_name()
