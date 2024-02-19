#!/usr/bin/python3
"""the class for the sqlalchemy library"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class DBStorage:
    """the class that creates tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        host = getenv("HBNB_MYSQL_HOST")
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """the method that returns a dictionary of the object"""
        my_dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query_db = self.__session.query(cls)

            for item in query_db:
                ky = "{}.{}".format(type(item).__name__, item.id)
                my_dic[ky] = item
        else:
            list_a = [State, City, User, Place, Review, Amenity]
            for clas in list_a:
                query_db = self.__session.query(clas)
                for item in query_db:
                    ky = "{}.{}".format(type(item).__name__, item.id)
                    my_dic[ky] = item
        return (my_dic)

    def new(self, ins):
        """the method that adds a new elem in the table"""
        self.__session.add(ins)

    def save(self):
        """the method that save changes to the table"""
        self.__session.commit()

    def delete(self, obj=None):
        """the method that deletes an elem in the table"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """the method used for the configuration"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        """the method that invokes remove()"""
        self.__session.close()
