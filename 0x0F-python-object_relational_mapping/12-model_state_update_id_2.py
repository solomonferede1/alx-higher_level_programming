#!/usr/bin/python3
"""
================================
11-medel_state_update_id_2 module
Update a state in the database
================================
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def update_state_name():
    """prints the first State object from the database"""
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_mexico = session.query(State).filter(State.id == 2).first()
    new_mexico.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    update_state_name()
