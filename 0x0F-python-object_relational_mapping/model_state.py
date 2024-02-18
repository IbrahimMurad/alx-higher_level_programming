""" This module defines a calss named State
and uses sqlalchemy to connect it to a table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Connects to table in a mysql database
The table name is states

Args:
    id (INTEGER): state id
    name (CHAR128): the name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
