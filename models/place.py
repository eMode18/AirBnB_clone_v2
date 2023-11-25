#!/usr/bin/python3
"""Defines the Place class."""
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
import models
from models.amenity import Amenity
from models.review import Review

assoc_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """Attributes:
    __tablename__ (str): Denotes the table name in MySQL storing place information.
    amenities (relationship): Represents the connection between a place and its amenities.
    amenity_ids (list): Collection of IDs linked to various amenities.
    city_id (String): Identifies the city associated with the place.
    description (String): Brief depiction or details describing the place.
    latitude (Float): Indicates the latitude coordinate of the place.
    longitude (Float): Indicates the longitude coordinate of the place.
    max_guest (Integer): Specifies the maximum number of guests allowed at the place.
    name (String): The title or name given to the place.
    number_bathrooms (Integer): Represents the count of bathrooms available at the place.
    number_rooms (Integer): Reflects the count of rooms within the place.
    price_by_night (Integer): Indicates the nightly price for staying at the place.
    reviews (relationship): Represents the association between a place and its reviews.
    user_id (String): Identifies the user linked to the place.
    """

    __tablename__ = "places"
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    amenity_ids = []
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    description = Column(String(1024))
    latitude = Column(Float)
    longitude = Column(Float)
    max_guest = Column(Integer, default=0)
    name = Column(String(128), nullable=False)
    number_bathrooms = Column(Integer, default=0)
    number_rooms = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    reviews = relationship("Review", backref="place", cascade="delete")
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Obtian a list of all the linked Reviews."""
            review_dict = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_dict.append(review)
            return review_dict

        @property
        def amenities(self):
            """Retrieve/set the linked Amenities."""
            amenity_dict = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_dict.append(amenity)
            return amenity_dict

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
