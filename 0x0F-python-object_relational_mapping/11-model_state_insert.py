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

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    # New Row
    n_state = State(name='Louisiana')

    # Adding Row to State class
    session.add(n_state)

    new_row = session.query(State).filter(State.name == 'Louisiana')

    print('{}'.format(new_row[0].id))

    # Updating table state
    session.commit()

    session.close()
