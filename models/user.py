#!/usr/bin/python3
"""Defines the User entity."""
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel


class User(BaseModel, Base):
    """Represents a user entity in a MySQL database.

    Inherits from SQLAlchemy Base and associates with the MySQL table 'users'.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing user data.
        email: (sqlalchemy String): Email address of the user.
        password (sqlalchemy String): User's account password.
        first_name (sqlalchemy String): First name of the user.
        last_name (sqlalchemy String): Last name of the user.
        places (sqlalchemy relationship): Relationship between User and Place.
        reviews (sqlalchemy relationship): Relationship between User and Review.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
