#!/usr/bin/python3
"""Implementation of the DBStorage engine."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Represents a dynamic database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): Active SQLAlchemy engine instance.
        __session (sqlalchemy.Session): Active SQLAlchemy session instance.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new instance of the DBStorage."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieve objects of a specific class from the database session.

        If cls is unspecified, it queries all available object types.

        Returns:
            Dictionary mapping object names to their respective instances.
        """
        if cls is None:
            queried_objs = self.__session.query(State).all()
            queried_objs.extend(self.__session.query(City).all())
            queried_objs.extend(self.__session.query(User).all())
            queried_objs.extend(self.__session.query(Place).all())
            queried_objs.extend(self.__session.query(Review).all())
            queried_objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            queried_objs = self.__session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in queried_objs}

    def new(self, obj):
        """Add a new object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Remove an object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Initialize database tables and create a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the active SQLAlchemy session."""
        self.__session.close()
