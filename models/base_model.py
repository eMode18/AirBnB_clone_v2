#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

Base = declarative_base()

class BaseModel:
    """Defines the BaseModel class with essential attributes.

    Attributes:
        id (sqlalchemy String): The unique identifier for the BaseModel.
        created_at (sqlalchemy DateTime): Represents the creation datetime.
        updated_at (sqlalchemy DateTime): Indicates the last update datetime.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused arguments.
            **kwargs (dict): Key/val pairs of attributes for the instance.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, val)

    def save(self):
        """Update updated_at with the current datetime and save instance."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/val pair __class__ representing
        the class name of the object.
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = str(type(self).__name__)
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        dict_obj.pop("_sa_instance_state", None)
        return dict_obj

    def delete(self):
        """Delete the current instance from the storage."""
        models.storage.delete(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        dc = self.__dict__.copy()
        dc.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, dc)
