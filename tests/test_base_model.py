#!/usr/bin/python3
"""defines unittests for models/base_model.py

unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import os
import models
import unnittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel_instantiation(unittest.TestCase):
    """unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_str(self):
        self.assertEqual(datetime, type(BaseModel().created_at))
    
    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.asserLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dte = datetime.today()
        dte_repr = repr(dte)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dte
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dte_repr, bmstr)
        self.assertIn("'updated_at': " + dte_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        bm = BaseModel(id=None, bm.__dict__.values())
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dte)
        self.assertEqual(bm.updated_at, dte)

    def test_instantiation_with_None_kwargs(self):
        with self.asserRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        bm = BaseModel("12", id="345", created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at)

class TestBaseModel_save(unittest>TestCase):
    """unittest for testing the save method of the BaseModel class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_files(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", 'r') as file:
            self.assertIn(bmid, file.read())

class TestBaseModel_to_dict(unittest.TestCase):
    """unittest for testing to_dict method of the BaseModel class"""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", b,.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dte = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dte
        tdict = {
                'id': '123456',
                '__class__': 'BaseModel',                
                'created_at': dt.isoformat()                
                'updated_at': dt.isoformat()                
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_constrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict()), tdict)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    if__name__ == "__main__":
        unittest.main()



