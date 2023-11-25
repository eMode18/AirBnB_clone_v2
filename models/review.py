#!/usr/bin/python3
"""Defines the Review entity."""
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column


class Review(BaseModel, Base):
    """Represents a user review entity within a MySQL database.

    Inherits from SQLAlchemy Base and connects to the MySQL table 'reviews'.

    Attributes:
        __tablename__ (str): The table name in the MySQL database for storing reviews.
        text (sqlalchemy String): The content of the review.
        place_id (sqlalchemy String): ID of the place associated with the review.
        user_id (sqlalchemy String): ID of the user who created the review.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

