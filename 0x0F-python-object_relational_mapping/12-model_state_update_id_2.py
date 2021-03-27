#!/usr/bin/python3
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session()

    update_row = session.query(State).filter(State.id == 2).first()
    update_row.name = 'New Mexico'
    session.commit()

    session.close()
