#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex
from os import getenv


class State(BaseModel, Base):
    """this is the state class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:
        @property
        def cities(self):
            var = models.storage.all()
            list_a = []
            res = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    list_a.append(var[key])
            for elem in list_a:
                if (elem.state_id == self.id):
                    res.append(elem)
            return (res)
