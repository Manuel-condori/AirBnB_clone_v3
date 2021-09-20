#!/usr/bin/python3
"""
Contains the TestAppDocs classes
"""

from datetime import datetime
import inspect
import models
import pep8
import unittest
from api.v1 import app


class TestAppDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.app_f = inspect.getmembers(app, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that file conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test(self):
        """Test that test file conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_api/test_v1/test_app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_app_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(app.__doc__, None,
                         "app.py needs a docstring")
        self.assertTrue(len(app.__doc__) >= 1,
                        "app.py needs a docstring")

    def test_app_class_docstring(self):
        """Test for the app class docstring"""
        self.assertIsNot(app.__doc__, None,
                         "app class needs a docstring")
        self.assertTrue(len(app.__doc__) >= 1,
                        "app class needs a docstring")

    def test_app_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in TestAppDocs.app_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
