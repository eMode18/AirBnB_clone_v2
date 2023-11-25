#!/usr/bin/python3
"""City class definition."""
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column

class City(BaseModel, Base):
    """Represents city information within a MySQL database.

    Inherits from SQLAlchemy Base and establishes a link to the MySQL
    table 'cities'.

    Attributes:
        __tablename__ (str): Name of the table storing City data in MySQL.
        name (sqlalchemy String): Name of the City.
        state_id (sqlalchemy String): State ID associated with the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

