#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dikt = {}
        if cls:
            dictionary = self.__objects
            for ky in dictionary:
                partition = ky.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dikt[ky] = self.__objects[ky]
            return (dikt)
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            ky = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[ky] = obj

    def save(self):
        """Saves storage dictionary to file"""
        my_dikt = {}
        for ky, val in self.__objects.items():
            my_dikt[ky] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as fl:
            json.dump(my_dikt, fl)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as fl:
                for ky, val in (json.load(fl)).items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[ky] = val
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """the func that deletes existing elems"""
        if obj:
            ky = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[ky]

    def close(self):
        """the func that invokes relaod()"""
        self.reload()
