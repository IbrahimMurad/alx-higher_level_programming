#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine, orm

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.Session(engine)
    try:
        state = session.query(State).where(State.id == 1).one()
        print("{}: {}".format(state.id, state.name))
    except Exception:
        print("Nothing")
    session.close()
