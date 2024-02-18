#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine, orm

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.Session(engine)
    myState = sys.argv[4].split(";")[0].split("'")[0]
    try:
        state = session.query(State).where(State.name == myState).one()
        print("{}".format(state.id))
    except Exception:
        print("Nothing")
    session.close()
