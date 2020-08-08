#!/usr/bin/python3
""" lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State)\
        .filter(State.id == 2)\
        .first()
    state.name = "New Mexico"
    session.commit()
    session.close()
