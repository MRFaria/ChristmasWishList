from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String, Integer, Boolean
from sqlalchemy.orm import relationship
import cherrypy

# Helper to map and register a Python class a db table
Base = declarative_base()

class Wishlist(Base):
    __tablename__ = 'wishlist'
    id = Column(Integer, primary_key=True)
    value = Column(String)
    bought = Column(Boolean)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    child_id = Column(Integer, ForeignKey('wishlist.id'))

