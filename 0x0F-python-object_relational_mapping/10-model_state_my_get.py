#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    # HERE: no SQL query, only objects!
    first_state = session.query(State).filter(State.name == state_name).all()

    if bool(first_state) is True:
        print("{}".format(first_state[0].id))  # [[3, Texas],] str represe.
    else:
        print("Not found")
    session.close()
