#!/usr/bin/python3
"""
=====================================
100-relationship_states_cites module
=====================================
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
import sys


def create_state():
    """Create state"""
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, echo=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name="San Francisco", state=State(name="California"))
    session.add(new_city)
    session.commit()


if __name__ == "__main__":
    create_state()
