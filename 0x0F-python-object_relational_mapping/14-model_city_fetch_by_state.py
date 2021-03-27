#!/usr/bin/python3
"""write a script 14-model_city_fetch_by_state.py that prints all City objects
 from the database hbtn_0e_14_usa """
import sys
from model_state import Base, State
from model_city import City
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
    # HERE: no SQL query, only objects!
    result = (session.query(State, City).filter(State.id == City.state_id)
              .order_by(City.id).all())

    for row in result:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
    session.close()
