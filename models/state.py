#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """this is the state class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        varb = models.storage.all()
        list_a = []
        res = []
        for ky in varb:
            city = ky.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_a.append(varb[ky])
        for item in list_a:
            if (item.state_id == self.id):
                res.append(item)
        return (res)
