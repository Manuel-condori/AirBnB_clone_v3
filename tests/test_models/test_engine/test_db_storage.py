#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the tests"""
        cls.u1 = User(email='user1@gmail.com', password='123')
        cls.u1.save()
        cls.u2 = User(email='user2@gmail.com', password='123')
        cls.u2.save()
        cls.u3 = User(email='user3@gmail.com', password='123')
        cls.u3.save()
        cls.a1 = Amenity(name='wifi')
        cls.a1.save()
        cls.a2 = Amenity(name='tv')
        cls.a2.save()
        cls.a3 = Amenity(name='jacuzzi')
        cls.a3.save()
        cls.s1 = State(name='New State 01')
        cls.s1.save()
        cls.s2 = State(name='New State 02')
        cls.s2.save()
        models.storage.save()

    @classmethod
    def tearDownClass(cls):
        """Teardown class for thye tests"""
        cls.u1.delete()
        cls.u2.delete()
        cls.u3.delete()
        cls.a1.delete()
        cls.a2.delete()
        cls.a3.delete()
        cls.s1.delete()
        cls.s2.delete()
        models.storage.save()

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_get_user(self):
        """Test that get method retrieves the correct object"""
        user = models.storage.get('User', TestDBStorage.u1.id)
        self.assertEqual(user, TestDBStorage.u1)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_get_amenity(self):
        """Test that get method retrieves the correct object"""
        amenity = models.storage.get('Amenity', TestDBStorage.a2.id)
        self.assertEqual(amenity, TestDBStorage.a2)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_get_state(self):
        """Test that get method retrieves the correct object"""
        state = models.storage.get('State', TestDBStorage.s2.id)
        self.assertEqual(state, TestDBStorage.s2)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_count_amenities(self):
        """Test that count method counts all instances of Amenity"""
        amenities_count = len(models.storage.all('Amenity').keys())
        count = models.storage.count('Amenity')
        self.assertEqual(amenities_count, count)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_count_cities(self):
        """Test that count method counts all instances of City"""
        cities_count = len(models.storage.all('City').keys())
        count = models.storage.count('City')
        self.assertEqual(cities_count, count)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_count_places(self):
        """Test that count method counts all instances of Place"""
        places_count = len(models.storage.all('Place').keys())
        count = models.storage.count('Place')
        self.assertEqual(places_count, count)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_count_reviews(self):
        """Test that count method counts all instances of Review"""
        reviews_count = len(models.storage.all('Review').keys())
        count = models.storage.count('Review')
        self.assertEqual(reviews_count, count)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_count_states(self):
        """Test that count method counts all instances of State"""
        states_count = len(models.storage.all('State').keys())
        count = models.storage.count('State')
        self.assertEqual(states_count, count)

    @unittest.skipIf(models.storage_t != 'db', "not testing file storage")
    def test_count_users(self):
        """Test that count method counts all instances of User"""
        users_count = len(models.storage.all('User').keys())
        count = models.storage.count('User')
        self.assertEqual(users_count, count)
