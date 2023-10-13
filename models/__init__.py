#!/usr/bin/python3

"""Initialize the storage
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


cls_names = {"BaseModel": BaseModel, "User": User, "Place": Place,
             "State": State, "City": City, "Amenity": Amenity,
             "Review": Review}

storage = FileStorage()
storage.reload()
