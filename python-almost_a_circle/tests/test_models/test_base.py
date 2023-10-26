#!/usr/bin/python3
""" Test for base class """

from models.base import Base
from models.rectangle import Rectangle
import unittest

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)


class TestBase(unittest.TestCase):
    """ Test for initialization """

    def test_init(self):
        """ Test for initialization """
        new_obj = Base()
        self.assertEqual(new_obj._Base__nb_objects, 1)
        self.assertEqual(new_obj.id, 1)
        new_obj_2 = Base()
        self.assertEqual(new_obj_2._Base__nb_objects, 2)
        self.assertEqual(new_obj_2.id, 2)
        new_obj_3 = Base(89)
        self.assertEqual(new_obj_3._Base__nb_objects, 2)
        self.assertEqual(new_obj_3.id, 89)

    """ Test for json string """

    def test_to_json_string(self):
        """ Test for json string
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dic = r1.to_dictionary()
        json = Base.to_json_string([dic])
        self.assertEqual(
            json, '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')

    def test_to_json_empty(self):
        """ Test for json string empty"""
        json = Base.to_json_string([])
        self.assertEqual(json, '[]')

    def test_to_json_none(self):
        """ Test for json string none"""
        json = Base.to_json_string(None)
        self.assertEqual(json, '[]')

    """ Test from json to string """

    def test_json_srting(self):
        """ Test for json string """
        json = Base.from_json_string(None)
        self.assertEqual(json, [])

    def test_json_str(self):
        """ Test for json string"""
        json = Base.from_json_string("[]")
        self.assertEqual(json, [])

    def test_json_str_good(self):
        """ Test for json string good
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_li_input = Base.to_json_string(list_input)
        json_output = Base.from_json_string(json_li_input)
        self.assertIsInstance(json_output, list)

    def test_json_str_empty(self):
        """ Test for json string empty"""
        json = Base.from_json_string(None)
        self.assertEqual(json, [])

    def test_json_str_empty_2(self):
        """ Test for json string empty"""
        json = Base.from_json_string("[]")
        self.assertEqual(json, [])


if __name__ == '__main__':
    unittest.main()
