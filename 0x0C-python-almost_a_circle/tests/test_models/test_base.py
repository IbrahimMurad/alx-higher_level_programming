""" This module is a test suit for Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test suits for Base class """

    # setting up before and tearing down after each test

    def setUp(self):
        """ starts a new connection """

        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """ Removes all the connections (restoring the initial state)"""

        pass

    def test_Base_a0(self):
        """ Check if value of __nd_objects before any calls """

        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_Base_a1(self):
        """ checks if Base has the private attribute __nb_objects """

        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_Base_a2(self):
        """ checks the type of the instance created and its id value """

        my_base = Base()
        self.assertEqual(str(type(my_base)), "<class 'models.base.Base'>")
        self.assertEqual(my_base.id, 1)
        self.assertEqual(my_base.__dict__, {'id': 1})

    def test_Base_a3(self):
        """ testing __init__ with zero arguments """

        with self.assertRaises(TypeError) as excpt:
            Base.__init__()
        the_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), the_msg)

    def test_Base_a4(self):
        """ testing __init__ with self and 2 more arguments"""

        with self.assertRaises(TypeError) as excpt:
            Base.__init__(self, 1, 2)
        the_msg = "__init__() takes from 1 to 2 positional arguments"
        the_msg += " but 3 were given"
        self.assertEqual(str(excpt.exception), the_msg)

    def test_Base_a5(self):
        """ checks id value afte mutiple calls """

        my_base = Base()
        my_base2 = Base()
        my_base3 = Base(12)
        my_base4 = Base('3')
        my_base5 = Base()
        self.assertEqual(my_base5.id, 3)

    def test_Base_a6(self):
        """ compares the id value of a call with the previous call """

        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_Base_a7(self):
        """ compares the id value of a call (withour argument)
        with __nb_objects value """

        my_base = Base()
        self.assertEqual(my_base.id, getattr(Base, "_Base__nb_objects"))

    def test_Base_a8(self):
        """ compares the id value of a call (withour argument)
        with __nb_objects value after multiple calls """

        base1 = Base()
        base2 = Base()
        base3 = Base(12)
        base4 = Base('13')
        base5 = Base()
        self.assertEqual(base5.id, getattr(Base, "_Base__nb_objects"))

    def test_Base_a9(self):
        """ testing a call with passed int value """

        theValue = 17
        my_base = Base(theValue)
        self.assertEqual(my_base.id, theValue)

    def test_Base_b0(self):
        """ testing a call with passed large int value """

        theValue = 654
        my_base = Base(theValue)
        self.assertEqual(my_base.id, theValue)

    def test_Base_b1(self):
        """ testing a call with passed non-int value """

        theValue = "blah"
        my_base = Base(theValue)
        self.assertEqual(my_base.id, theValue)


if __name__ == '__main__':
    unittest.main()
