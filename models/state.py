#!/usr/bin/python3
"""State class definition."""
import models
from os import getenv
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City


class State(BaseModel, Base):
    """Represents state information within a MySQL database.

    Get properties from SQLAlchemy Base and establishes a
    link to the MySQL table 'states'.

    Attributes:
        __tablename__ (str): Name of the table storing State data in MySQL.
        name (sqlalchemy String): Name of the State.
        cities (sqlalchemy relationship): Relationship between State and City.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Retrieve a list of associated City objects."""
            city_arr = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_arr.append(city)
            return city_arr
