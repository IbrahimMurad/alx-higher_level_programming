import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange

class TestBase(unittest.TestCase):
     
    # setting up before and tearing down after each test

    def setUp(self):
        """ starts a new connection """

        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """ Removes all the connections (restoring the initial state)"""

        pass


    """ testing __init__ """
  
    # passing: width and height
    def test_Rectangle_a0(self):
        """ what is Rectangle """

        self.assertEqual(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_Rectangle_a1(self):
        """ checking to ensure that Rectangle is a subclass of Base """

        self.assertTrue(issubclass(Rectangle, Base))

    def test_Rectangle_a2(self):
        """ testing a call with 0 arguments (self excluded) """

        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle()
        excpt_msg = "__init__() missing 2 required positional arguments:"
        excpt_msg += " 'width' and 'height'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_a3(self):
        """ testing a call with 1 arguments (self excluded) """

        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(2)
        excpt_msg = "__init__() missing 1 required positional argument:"
        excpt_msg += " 'height'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_a3(self):
        """ testing a call with more than required arguments
        (self excluded) """

        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(2, 2, 3, 3, 5, 13)
        excpt_msg = "__init__() takes from 3 to 6 positional arguments "
        excpt_msg += "but 7 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_a4(self):
        """ testing the type of an instance """

        my_rect = Rectangle(1, 1)
        self.assertTrue(type(my_rect) is Rectangle)
        self.assertTrue(isinstance(my_rect, Rectangle))
        self.assertTrue(isinstance(my_rect, Base))
        self.assertEqual(str(type(my_rect)), "<class 'models.rectangle.Rectangle'>")

    def test_Rectangle_a5(self):
        """ checing the default values and passed values """
        
        my_rect = Rectangle(12, 15)
        my_rect_dict = {'id': 1, '_Rectangle__width': 12, '_Rectangle__height': 15,
                        '_Rectangle__x': 0, '_Rectangle__y': 0}
        self.assertEqual(my_rect.__dict__, my_rect_dict)
        self.assertEqual(my_rect.id, 1)
        self.assertEqual(my_rect.x, 0)
        self.assertEqual(my_rect.y, 0)
        self.assertEqual(my_rect.width, 12)
        self.assertEqual(my_rect.height, 15)

    def test_Rectangle_a6(self):
        """ testing non-int width """

        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle('2', 2)
        excpt_msg = "width must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(2.0, 2)
        excpt_msg = "width must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(2.0, 2.0)
        excpt_msg = "width must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_a7(self):
        """ testing non-int height """

        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(2, '2')
        excpt_msg = "height must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(2, 2.0)
        excpt_msg = "height must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_a8(self):
        """ testing non-int x """

        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(20, 12, '1')
        excpt_msg = "x must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(20, 12, 1.0)
        excpt_msg = "x must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_a9(self):
        """ testing non-int y """

        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(20, 12, 3, '1')
        excpt_msg = "y must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_rect = Rectangle(20, 12, 4, 1.0)
        excpt_msg = "y must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_b0(self):
        """ testing unacceptable value of width """

        with self.assertRaises(ValueError) as excpt:
            my_rect = Rectangle(0, 2)
        excpt_msg = "width must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(ValueError) as excpt:
            my_rect = Rectangle(-2, 2)
        excpt_msg = "width must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_b1(self):
        """ testing unacceptable value of height """

        with self.assertRaises(ValueError) as excpt:
            my_rect = Rectangle(2, 0)
        excpt_msg = "height must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(ValueError) as excpt:
            my_rect = Rectangle(2, -2)
        excpt_msg = "height must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_b2(self):
        """ testing non-int x """

        with self.assertRaises(ValueError) as excpt:
            my_rect = Rectangle(20, 12, -2)
        excpt_msg = "x must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_b3(self):
        """ testing non-int y """

        with self.assertRaises(ValueError) as excpt:
            my_rect = Rectangle(20, 12, 3, -2)
        excpt_msg = "y must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_b4(self):
        """ comparing id value with _base__nb_objects """
        
        my_rect1 = Rectangle(5, 3, 2, 2)
        my_rect2 = Rectangle(5, 3, 2, 2, 11)
        self.assertEqual(my_rect1.id, getattr(Base, "_Base__nb_objects"))
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 1)

    def test_Rectangle_b5(self):
        """ checing the passed values non-keyworded """
        
        my_rect = Rectangle(12, 15, 40, 20, 5248)
        my_rect_dict = {'id': 5248, '_Rectangle__width': 12, '_Rectangle__height': 15,
                        '_Rectangle__x': 40, '_Rectangle__y': 20}
        self.assertEqual(my_rect.__dict__, my_rect_dict)
        self.assertEqual(my_rect.id, 5248)
        self.assertEqual(my_rect.x, 40)
        self.assertEqual(my_rect.y, 20)
        self.assertEqual(my_rect.width, 12)
        self.assertEqual(my_rect.height, 15)

    def test_Rectangle_b6(self):
        """ checing the passed values keyworded """
        
        my_rect = Rectangle(12, 15, x=40, y=20, id=5248)
        my_rect_dict = {'id': 5248, '_Rectangle__width': 12, '_Rectangle__height': 15,
                        '_Rectangle__x': 40, '_Rectangle__y': 20}
        self.assertEqual(my_rect.__dict__, my_rect_dict)
        self.assertEqual(my_rect.id, 5248)
        self.assertEqual(my_rect.x, 40)
        self.assertEqual(my_rect.y, 20)
        self.assertEqual(my_rect.width, 12)
        self.assertEqual(my_rect.height, 15)

    def test_Rectangle_b7(self):
        """ checing the id value after setting it from Base """
        
        Base._Base__nb_objects = 99
        my_rect = Rectangle(12, 15)
        self.assertEqual(my_rect.id, 100)
        self.assertEqual(my_rect.id, getattr(Base, "_Base__nb_objects"))

    def test_Rectangle_b8(self):
        """ checking getter and setter """

        my_rect = Rectangle(1, 2, 3, 4)
        my_rect.width = 11
        my_rect.height = 12
        my_rect.x = 13
        my_rect.y = 14
        self.assertEqual(my_rect.width, 11)
        self.assertEqual(my_rect.height, 12)
        self.assertEqual(my_rect.x, 13)
        self.assertEqual(my_rect.y, 14)

    def test_Rectangle_b9(self):
        """ checking area method """

        my_rect = Rectangle(1, 2)
        self.assertEqual(my_rect.area(), 1 * 2)
        my_rect = Rectangle(100, 123)
        self.assertEqual(my_rect.area(), 100 * 123)

    def test_Rectangle_c0(self):
        """ more checking for area method """

        my_rect = Rectangle(1, 2)
        with self.assertRaises(TypeError) as excpt:
            Rectangle.area()
        excpt_msg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_c0(self):
        '''Tests area() method compuation.'''
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * h)

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

if __name__ == '__main__':
    unittest.main()
