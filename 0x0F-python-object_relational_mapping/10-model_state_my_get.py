#!/usr/bin/python3
""" that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
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
    query = session.query(State).\
        filter(State.name.like('{}'.format(argv[4]))).\
        first()
    if query:
        print("{}".format(query.id))
    else:
        print("Not found")
    session.close()
