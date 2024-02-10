#!/usr/bin/python3
import uuid
from datetime import datetime
"""importing modules"""


class BaseModel:
    """class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """A method is useful to do any initialization passing initial values
        to your object you want to do with your object"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            del kwargs["__class__"]
            for k, v in kwargs.items():
                if k == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["updated_at"], time)
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], time)
            else:
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """method returns a human-readable, or
        informal, string representation of an object"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        mydict = self.__dict__.copy()
        new_dict = {**mydict, **{"__class__": self.__class__.__name__},
                    **{"created_at": self.created_at.isoformat()},
                    **{"updated_at": self.updated_at.isoformat}}
        return new_dict
