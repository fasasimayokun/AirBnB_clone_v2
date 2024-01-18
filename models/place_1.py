#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Table, Float, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """the class  place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        aenities = relationship("Amenity", secondary=place_amenity,
                                viewonly=False,
                                back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """the property that returns list of reviews.id"""
            varb = models.storage.all()
            list_a = []
            res = []
            for ky in varb:
                review = ky.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    list_a.append(varb[ky])
            for item in list_a:
                if (item.place_id == self.id):
                    res.append(item)
            return (res)

        @property
        def amenities(self):
            """the property that returns list of amenity.id"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """the setter method that appends the amenity id to the attr"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
