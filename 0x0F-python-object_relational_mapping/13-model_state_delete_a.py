#!/usr/bin/python3
"""a script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa"""
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

    session = Session(engine)

    row_a = session.query(State).filter(State.name.like('%a%')).all()

    for row in row_a:
        session.delete(row)

    session.commit()

    session.close()
