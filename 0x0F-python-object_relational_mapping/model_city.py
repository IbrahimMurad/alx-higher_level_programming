#!/usr/bin/python3
""" This module defines a calss named State
and uses sqlalchemy to connect it to a table states
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Connects to table in a mysql database
The table name is cities

Args:
    id (INTEGER): state id
    name (CHAR128): the name of the state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False,)
