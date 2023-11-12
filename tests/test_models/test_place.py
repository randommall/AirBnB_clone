#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class.
    """

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

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(my_place))
        self.assertNotIn("city_id", my_place.__dict__)

    def test_user_id_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(my_place))
        self.assertNotIn("user_id", my_place.__dict__)

    def test_name_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(my_place))
        self.assertNotIn("name", my_place.__dict__)

    def test_description_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(my_place))
        self.assertNotIn("desctiption", my_place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(my_place))
        self.assertNotIn("number_rooms", my_place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(my_place))
        self.assertNotIn("number_bathrooms", my_place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(my_place))
        self.assertNotIn("max_guest", my_place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(my_place))
        self.assertNotIn("price_by_night", my_place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(my_place))
        self.assertNotIn("latitude", my_place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(my_place))
        self.assertNotIn("longitude", my_place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(my_place))
        self.assertNotIn("amenity_ids", my_place.__dict__)

    def test_two_places_unique_ids(self):
        my_place1 = Place()
        my_place2 = Place()
        self.assertNotEqual(my_place1.id, my_place2.id)

    def test_two_places_different_created_at(self):
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.created_at, my_place2.created_at)

    def test_two_places_different_updated_at(self):
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.updated_at, my_place2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        my_place = Place()
        my_place.id = "777777"
        my_place.created_at = my_place.updated_at = my_date
        my_place_str = my_place.__str__()
        self.assertIn("[Place] (777777)", my_place_str)
        self.assertIn("'id': '777777'", my_place_str)
        self.assertIn("'created_at': " + my_date_repr, my_place_str)
        self.assertIn("'updated_at': " + my_date_repr, my_place_str)

    def test_args_unused(self):
        my_place = Place(None)
        self.assertNotIn(None, my_place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        my_place = Place(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(my_place.id, "777")
        self.assertEqual(my_place.created_at, my_date)
        self.assertEqual(my_place.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    Unittests for testing save method of the Place class.
    """

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
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        self.assertLess(first_updated_at, my_place.updated_at)

    def test_two_saves(self):
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        second_updated_at = my_place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_place.save()
        self.assertLess(second_updated_at, my_place.updated_at)

    def test_save_with_arg(self):
        my_place = Place()
        with self.assertRaises(TypeError):
            my_place.save(None)

    def test_save_updates_file(self):
        my_place = Place()
        my_place.save()
        my_place_id = "Place." + my_place.id
        with open("file.json", "r") as f:
            self.assertIn(my_place_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Place class.
    """

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

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        my_place = Place()
        self.assertIn("id", my_place.to_dict())
        self.assertIn("created_at", my_place.to_dict())
        self.assertIn("updated_at", my_place.to_dict())
        self.assertIn("__class__", my_place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        my_place = Place()
        my_place.middle_name = "Johnson"
        my_place.my_number = 777
        self.assertEqual("Johnson", my_place.middle_name)
        self.assertIn("my_number", my_place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        my_place = Place()
        my_place_dict = my_place.to_dict()
        self.assertEqual(str, type(my_place_dict["id"]))
        self.assertEqual(str, type(my_place_dict["created_at"]))
        self.assertEqual(str, type(my_place_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        my_place = Place()
        my_place.id = "777777"
        my_place.created_at = my_place.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Place',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(my_place.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        my_place = Place()
        self.assertNotEqual(my_place.to_dict(), my_place.__dict__)

    def test_to_dict_with_arg(self):
        my_place = Place()
        with self.assertRaises(TypeError):
            my_place.to_dict(None)


if __name__ == "__main__":
    unittest.main()