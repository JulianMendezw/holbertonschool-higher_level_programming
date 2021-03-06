#!/usr/bin/python3
"""Unittest for rectangle.py"""


import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """
    Define TestRectangleClass
    """

    def test_id(self):
        """
        Testing valid id
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 15)

    def test_display(self):
        """
        Testing display
        """
        r1 = Rectangle(2, 2, 2, 2)
        display = ('\n' * 2 + (((' ' * 2) + '#' * 2 + '\n') * 2))
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        out = f.getvalue()
        self.assertEqual(out, display)

    def test_ids(self):
        """
        Testing valid ids
        """
        r2 = Rectangle(32, 2)
        self.assertEqual(r2.id, 16)
        r3 = Rectangle(7, 2)
        self.assertEqual(r3.id, 17)
        r4 = Rectangle(32, 3, 0, 0, 77)
        self.assertEqual(r4.id, 77)

    def test_valid_params(self):
        """
        Testing with valid parameters
        """
        r5 = Rectangle(3, 5, 2, 8, 108)
        self.assertEqual([r5.width, r5.height, r5.x, r5.y, r5.id],
                         [3, 5, 2, 8, 108])
        r6 = Rectangle(43, 23)
        self.assertEqual([r6.width, r6.height], [43, 23])

    def test_params_defaults(self):
        """
        Testing default values for x, y
        """
        r7 = Rectangle(32, 12)
        self.assertEqual([r7.x, r7.y], [0, 0])

    def test_params_defaults_2(self):
        """
        Testing default params
        """
        r8 = Rectangle(32, 32, 13)
        self.assertEqual([r8.width, r8.height, r8.x, r8.y, r8.id],
                         [32, 32, 13, 0, 19])

    def test_params_setters(self):
        """
        Testing all setters
        """
        r9 = Rectangle(32, 34)
        r9.width = 21
        self.assertEqual(r9.width, 21)
        r9.height = 87
        self.assertEqual(r9.height, 87)
        r9.x = 55
        self.assertEqual(r9.x, 55)
        r9.y = 444
        self.assertEqual(r9.y, 444)

    def test_params_exceptions_args(self):
        """Checks wrong number of arguments, zero"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_params_exceptions_args_one(self):
        """Checks wrong number of arguments, 1 args"""
        with self.assertRaises(TypeError):
            r = Rectangle(21)

    def test_params_exceptions_args_six(self):
        """
        Checks wrong number of arguments, six
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 23, 12, 234, 4)

    def test_args_value_zero(self):
        """
        Testing valid value
        """
        errormsg = " must be > 0"
        err = ValueError
        try:
            Rectangle(-10, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + errormsg)
        try:
            Rectangle(10, -10)
        except err as e:
            self.assertEqual((str(e)), "height" + errormsg)
        try:
            Rectangle(0, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + errormsg)
        try:
            Rectangle(10, 0)
        except err as e:
            self.assertEqual((str(e)), "height" + errormsg)
        errormsg = " must be >= 0"
        try:
            Rectangle(10, 10, -2)
        except err as e:
            self.assertEqual((str(e)), "x" + errormsg)
        try:
            Rectangle(10, 10, 2, -3)
        except err as e:
            self.assertEqual((str(e)), "y" + errormsg)


if __name__ == "__main__":
    unittest.main()
