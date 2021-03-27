#!/usr/bin/python3
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import update
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    update_row = session.query(State).get(2)
    update_row.name = 'New Mexico'
    session.commit()

    session.close()
