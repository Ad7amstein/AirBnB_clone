#!/usr/bin/python3
"""Defines Unittest for base module."""

import unittest
import os
import datetime
import pycodestyle
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Test suits for base module functiosn."""

    def setUp(self):
        """Executes before any test."""
        FileStorage.__objects = None
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_shebang(self):
        """Test shebang."""
        with open('models/base_model.py', 'r') as file:
            line = file.readline()
            self.assertMultiLineEqual(line, '#!/usr/bin/python3\n')

    def test_pycodestyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_function_existence(self):
        """Test function existence"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_attributes_existence(self):
        """Test attributes existence"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_docstring(self):
        """Test the documentation of modules and function."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """Test the attributes."""
        b1 = BaseModel()
        b1.name = "My First Model"
        b1.my_number = 89
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime.datetime)
        self.assertIsInstance(b1.updated_at, datetime.datetime)
        self.assertIsInstance(b1.name, str)
        self.assertIsInstance(b1.my_number, int)

    def test_to_dict(self):
        """Test to_dict method."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertIsInstance(my_model_json["id"], str)
        self.assertIsInstance(my_model_json["created_at"], str)
        self.assertIsInstance(my_model_json["updated_at"], str)
        self.assertIsInstance(my_model_json["__class__"], str)
        self.assertIsInstance(my_model_json["name"], str)
        self.assertIsInstance(my_model_json["my_number"], int)
        self.assertDictEqual(my_model_json,
                             {"id": my_model.id,
                              "created_at": my_model.created_at.isoformat(),
                              "updated_at": my_model.updated_at.isoformat(),
                              "__class__": my_model.__class__.__name__,
                              "name": my_model.name,
                              "my_number": my_model.my_number})
        b2 = BaseModel(**my_model_json)
        self.assertIsInstance(b2.id, str)
        self.assertIsInstance(b2.created_at, datetime.datetime)
        self.assertIsInstance(b2.updated_at, datetime.datetime)
        self.assertIsInstance(b2.name, str)
        self.assertIsInstance(b2.my_number, int)
        self.assertEqual(my_model.id, b2.id)
        self.assertEqual(my_model.created_at, b2.created_at)
        self.assertEqual(my_model.updated_at, b2.updated_at)
        self.assertEqual(my_model.name, b2.name)
        self.assertEqual(my_model.my_number, b2.my_number)

        self.assertFalse(my_model is b2)

    def test_str(self):
        """Test __str__ method."""
        b1 = BaseModel()
        b1.name = "My First Model"
        b1.my_number = 89
        string = "[{}] ({}) {}".format(type(b1).__name__, b1.id, b1.__dict__)
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """Test save method."""
        b1 = BaseModel()
        time_before = b1.updated_at
        b1.save()
        time_after = b1.updated_at
        self.assertNotEqual(time_before, time_after)
