#!/usr/bin/python3
"""
Module for City unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """
    Unittests for instantiation of the City class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        my_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(my_city))
        self.assertNotIn("state_id", my_city.__dict__)

    def test_name_is_public_class_attribute(self):
        my_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(my_city))
        self.assertNotIn("name", my_city.__dict__)

    def test_two_cities_unique_ids(self):
        my_city1 = City()
        my_city2 = City()
        self.assertNotEqual(my_city1.id, my_city2.id)

    def test_two_cities_different_created_at(self):
        my_city1 = City()
        sleep(0.05)
        my_city2 = City()
        self.assertLess(my_city1.created_at, my_city2.created_at)

    def test_two_cities_different_updated_at(self):
        my_city1 = City()
        sleep(0.05)
        my_city2 = City()
        self.assertLess(my_city1.updated_at, my_city2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        my_city = City()
        my_city.id = "777777"
        my_city.created_at = my_city.updated_at = my_date
        my_city_str = my_city.__str__()
        self.assertIn("[City] (777777)", my_city_str)
        self.assertIn("'id': '777777'", my_city_str)
        self.assertIn("'created_at': " + my_date_repr, my_city_str)
        self.assertIn("'updated_at': " + my_date_repr, my_city_str)

    def test_args_unused(self):
        my_city = City(None)
        self.assertNotIn(None, my_city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        my_city = City(id="345", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(my_city.id, "345")
        self.assertEqual(my_city.created_at, my_date)
        self.assertEqual(my_city.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        my_city = City()
        sleep(0.05)
        first_updated_at = my_city.updated_at
        my_city.save()
        self.assertLess(first_updated_at, my_city.updated_at)

    def test_two_saves(self):
        my_city = City()
        sleep(0.05)
        first_updated_at = my_city.updated_at
        my_city.save()
        second_updated_at = my_city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_city.save()
        self.assertLess(second_updated_at, my_city.updated_at)

    def test_save_with_arg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            my_city.save(None)

    def test_save_updates_file(self):
        my_city = City()
        my_city.save()
        my_city_id = "City." + my_city.id
        with open("file.json", "r") as f:
            self.assertIn(my_city_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        my_city = City()
        self.assertIn("id", my_city.to_dict())
        self.assertIn("created_at", my_city.to_dict())
        self.assertIn("updated_at", my_city.to_dict())
        self.assertIn("__class__", my_city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        my_city = City()
        my_city.middle_name = "Johnson"
        my_city.my_number = 777
        self.assertEqual("Johnson", my_city.middle_name)
        self.assertIn("my_number", my_city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        my_city = City()
        my_city_dict = my_city.to_dict()
        self.assertEqual(str, type(my_city_dict["id"]))
        self.assertEqual(str, type(my_city_dict["created_at"]))
        self.assertEqual(str, type(my_city_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        my_city = City()
        my_city.id = "123456"
        my_city.created_at = my_city.updated_at = my_date
        to_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(my_city.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        my_city = City()
        self.assertNotEqual(my_city.to_dict(), my_city.__dict__)

    def test_to_dict_with_arg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            my_city.to_dict(None)


if __name__ == "__main__":
    unittest.main()