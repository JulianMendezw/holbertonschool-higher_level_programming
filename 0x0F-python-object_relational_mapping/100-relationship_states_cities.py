#!/usr/bin/python3
"""Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name='California')
    new_state.cities = [City(name='San Francisco')]

    session.add(new_state)
    session.commit()
    session.close()
