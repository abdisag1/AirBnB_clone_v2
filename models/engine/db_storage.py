#!/usr/bin/python3
<<<<<<< HEAD
"""SQL db engine class"""
import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
=======
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
>>>>>>> 45086d9d76cb88c7d6863db7478aebd63d704c1f
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """SQL db class"""
=======
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

>>>>>>> 45086d9d76cb88c7d6863db7478aebd63d704c1f
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Instantiation"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                      os.getenv("HBNB_MYSQL_USER"),
                                      os.getenv("HBNB_MYSQL_PWD"),
                                      os.getenv("HBNB_MYSQL_HOST"),
                                      os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """All"""
        res_dict = {}
        temp = []

        if cls is not None:
            temp = self.__session.query(cls).all()
        else:
            temp += self.__session.query(User).all()
            temp += self.__session.query(State).all()
            temp += self.__session.query(City).all()
            temp += self.__session.query(Amenity).all()
            temp += self.__session.query(Place).all()
            temp += self.__session.query(Review).all()
        for i in temp:
            key = "{}.{}".format(i.__class__.__name__, i.id)
            res_dict[key] = i

        return res_dict

    def new(self, obj):
        """New"""
        try:
            self.__session.add(obj)
        except:
            pass

    def save(self):
        """Save"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete"""
=======
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
>>>>>>> 45086d9d76cb88c7d6863db7478aebd63d704c1f
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
<<<<<<< HEAD
        """Reload"""
        Base.metadata.create_all(self.__engine)
        current = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(current)

    def close(self):
        """calls session close"""
=======
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
>>>>>>> 45086d9d76cb88c7d6863db7478aebd63d704c1f
        self.__session.close()
