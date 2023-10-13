#!/usr/bin/python3

"""Initialize the storage
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


cls_names = {"BaseModel": BaseModel, "User": User}

storage = FileStorage()
storage.reload()
