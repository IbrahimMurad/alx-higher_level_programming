import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io

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
    def test_Square_a0(self):
        """ what is Square """

        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_Square_a1(self):
        """ checking to ensure that Square is a subclass of Base """

        self.assertTrue(issubclass(Square, Base))

    def test_Square_a2(self):
        """ checking to ensure that Square is a subclass of Rectangle """

        self.assertTrue(issubclass(Square, Rectangle))


    def test_Square_a3(self):
        """ testing a call with 0 arguments (self excluded) """

        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square()
        excpt_msg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_a4(self):
        """ testing a call with more than required arguments
        (self excluded) """

        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square(2, 3, 3, 5, 13)
        excpt_msg = "__init__() takes from 2 to 5 positional arguments "
        excpt_msg += "but 6 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_a5(self):
        """ testing the type of an instance """

        my_sqr = Square(1, 1)
        self.assertTrue(type(my_sqr) is Square)
        self.assertTrue(isinstance(my_sqr, Square))
        self.assertTrue(isinstance(my_sqr, Rectangle))
        self.assertTrue(isinstance(my_sqr, Base))
        self.assertEqual(str(type(my_sqr)), "<class 'models.square.Square'>")

    def test_Square_a6(self):
        """ checing the default values and passed values """
        
        my_sqr = Square(4)
        my_sqr_dict = {'id': 1, '_Rectangle__width': 4, '_Rectangle__height': 4,
                        '_Rectangle__x': 0, '_Rectangle__y': 0}
        self.assertEqual(my_sqr.__dict__, my_sqr_dict)
        self.assertEqual(my_sqr.id, 1)
        self.assertEqual(my_sqr.x, 0)
        self.assertEqual(my_sqr.y, 0)
        self.assertEqual(my_sqr.width, 4)
        self.assertEqual(my_sqr.height, 4)

    def test_Square_a7(self):
        """ testing non-int width """

        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square('2')
        excpt_msg = "width must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square(2.0)
        excpt_msg = "width must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_a8(self):
        """ testing non-int x """

        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square(12, '1')
        excpt_msg = "x must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square(12, 1.0)
        excpt_msg = "x must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_a9(self):
        """ testing non-int y """

        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square(12, 3, '1')
        excpt_msg = "y must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(TypeError) as excpt:
            my_sqr = Square(12, 4, 1.0)
        excpt_msg = "y must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_b0(self):
        """ testing unacceptable value of width """

        with self.assertRaises(ValueError) as excpt:
           my_sqr = Square(0)
        excpt_msg = "width must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)
        
        with self.assertRaises(ValueError) as excpt:
            my_sqr = Square(-2)
        excpt_msg = "width must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_b1(self):
        """ testing non-int x """

        with self.assertRaises(ValueError) as excpt:
            my_sqr = Square(12, -2)
        excpt_msg = "x must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_b2(self):
        """ testing non-int y """

        with self.assertRaises(ValueError) as excpt:
           my_sqr = Square(12, 3, -2)
        excpt_msg = "y must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_b3(self):
        """ comparing id value with _base__nb_objects """
        
        my_sqr1 = Square(5, 3, 2)
        my_sqr2 = Square(5, 3, 2, 11)
        self.assertEqual(my_sqr1.id, getattr(Base, "_Base__nb_objects"))
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 1)

    def test_Square_b4(self):
        """ checing the passed values non-keyworded """
        
        my_sqr = Square(12, 40, 20, 5248)
        my_sqr_dict = {'id': 5248, '_Rectangle__width': 12, '_Rectangle__height': 12,
                        '_Rectangle__x': 40, '_Rectangle__y': 20}
        self.assertEqual(my_sqr.__dict__, my_sqr_dict)
        self.assertEqual(my_sqr.id, 5248)
        self.assertEqual(my_sqr.x, 40)
        self.assertEqual(my_sqr.y, 20)
        self.assertEqual(my_sqr.width, 12)
        self.assertEqual(my_sqr.height, 12)
        self.assertEqual(my_sqr.size, 12)

    def test_Square_b5(self):
        """ checing the passed values keyworded """
        
        my_sqr = Square(12, x=40, y=20, id=5248)
        my_sqr_dict = {'id': 5248, '_Rectangle__width': 12, '_Rectangle__height': 12,
                        '_Rectangle__x': 40, '_Rectangle__y': 20}
        self.assertEqual(my_sqr.__dict__, my_sqr_dict)
        self.assertEqual(my_sqr.id, 5248)
        self.assertEqual(my_sqr.x, 40)
        self.assertEqual(my_sqr.y, 20)
        self.assertEqual(my_sqr.width, 12)
        self.assertEqual(my_sqr.height, 12)
        self.assertEqual(my_sqr.size, 12)

    def test_Square_b6(self):
        """ checing the id value after setting it from Base """
        
        Base._Base__nb_objects = 99
        my_sqr = Square(12, 15)
        self.assertEqual(my_sqr.id, 100)
        self.assertEqual(my_sqr.id, getattr(Base, "_Base__nb_objects"))

    def test_Square_b7(self):
        """ checking getter and setter """

        my_sqr = Square(7, 3, 4)
        my_sqr.size = 7
        my_sqr.x = 13
        my_sqr.y = 14
        self.assertEqual(my_sqr.size, 7)
        self.assertEqual(my_sqr.width, 7)
        self.assertEqual(my_sqr.height, 7)
        self.assertEqual(my_sqr.x, 13)
        self.assertEqual(my_sqr.y, 14)

    def test_Square_b8(self):
        """ checking area method """

        my_sqr = Square(1)
        self.assertEqual(my_sqr.area(), 1 ** 2)
        my_sqr = Square(100)
        self.assertEqual(my_sqr.area(), 100 ** 2)

    def test_Square_b9(self):
        """ more checking for area method """

        my_sqr = Square(2)
        with self.assertRaises(TypeError) as excpt:
            Square.area()
        excpt_msg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_c1(self):
        """ Testing display method: with only width and height """

        my_rect = Rectangle(1,1)
        with self.assertRaises(TypeError) as excpt:
            Rectangle.display()
        excpt_msg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_c2(self):
        """ Testing display method: with only width and height
        x = 0 and y = 0 """

        my_rect = Rectangle(1,1)
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "#\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.width = 5
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "#####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.height = 3
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "#####\n#####\n#####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.width = 5
        my_rect.height = 1
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "#####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.width = 1
        my_rect.height = 5
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "#\n#\n#\n#\n#\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.width = 10
        my_rect.height = 10
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "##########\n\
##########\n\
##########\n\
##########\n\
##########\n\
##########\n\
##########\n\
##########\n\
##########\n\
##########\n"
        self.assertEqual(my_IO.getvalue(), my_out)

    def test_Rectangle_c3(self):
        """ Testing display method: x and y included """

        my_rect = Rectangle(1,1, 1, 1)
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "\n #\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.width = 5
        my_rect.height = 3
        my_rect.x = 0
        my_rect.y = 5
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "\n\n\n\n\n#####\n#####\n#####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.x = 5
        my_rect.y = 0
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "     #####\n     #####\n     #####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.x = 3
        my_rect.y = 3
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "\n\n\n   #####\n   #####\n   #####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_rect.x = 18
        my_rect.y = 10
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_rect.display()
        my_out = "\n\n\n\n\n\n\n\n\n\n\
                  #####\n\
                  #####\n\
                  #####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

    def test_Rectangle_c4(self):
        """ Testing __str__: without passing self """

        my_rect = Rectangle(1,1, 1, 1)
        with self.assertRaises(TypeError) as excpt:
            Rectangle.__str__()
        excpt_msg = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_c5(self):
        """ Testing __str__: with different attributes values """

        my_rect = Rectangle(15,13)
        my_out = "[Rectangle] (1) 0/0 - 15/13"
        self.assertEqual(str(my_rect), my_out)

        my_rect = Rectangle(15,13, 10, 5)
        my_out = "[Rectangle] (2) 10/5 - 15/13"
        self.assertEqual(str(my_rect), my_out)
        
        my_rect = Rectangle(15,13, 3)
        my_out = "[Rectangle] (3) 3/0 - 15/13"
        self.assertEqual(str(my_rect), my_out)
        
        my_rect = Rectangle(15,13, 10, 5, 'superID')
        my_out = "[Rectangle] (superID) 10/5 - 15/13"
        self.assertEqual(str(my_rect), my_out)

    def test_Rectangle_c6(self):
        """ Testing update method: without self as an argument """

        with self.assertRaises(TypeError) as excpt:
            Rectangle.update()
        excpt_msg = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_c7(self):
        """ Testing update method (args): with differenct values """

        rect1 = Rectangle(10, 10, 10, 10)
        init_rect_dict = rect1.__dict__
        rect1.update(89)
        init_rect_dict['id'] = 89
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2)
        init_rect_dict['_Rectangle__width'] = 2
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2, 3)
        init_rect_dict['_Rectangle__height'] = 3
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2, 3, 4)
        init_rect_dict['_Rectangle__x'] = 4
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2, 3, 4, 5)
        init_rect_dict['_Rectangle__y'] = 5
        self.assertEqual(rect1.__dict__, init_rect_dict)

    def test_Rectangle_c8(self):
        """ Testing update method (args): with bad values """

        rect1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as excpt:
            rect1.update(10, '1')
        excpt_msg = "width must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        with self.assertRaises(TypeError) as excpt:
            rect1.update(10, 2, '3')
        excpt_msg = "height must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        with self.assertRaises(TypeError) as excpt:
            rect1.update(10, 2, 3, '4')
        excpt_msg = "x must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)
        with self.assertRaises(TypeError) as excpt:
            rect1.update(89, 2, 3, 4, '5')
        excpt_msg = "y must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

        rect1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError) as excpt:
            rect1.update(10, -2)
        excpt_msg = "width must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)
        with self.assertRaises(ValueError) as excpt:
            rect1.update(10, 2, -3)
        excpt_msg = "height must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)
        with self.assertRaises(ValueError) as excpt:
            rect1.update(10, 2, 3, -4)
        excpt_msg = "x must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)
        with self.assertRaises(ValueError) as excpt:
            rect1.update(89, 2, 3, 4, -5)
        excpt_msg = "y must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_c9(self):
        """ Testing update method (kwargs): skipping kwargs """

        rect1 = Rectangle(10, 10, 10, 10)
        init_rect_dict = rect1.__dict__
        rect1.update(89, 2, 3, 4, 5, id=13)
        init_rect_dict['id'] = 89
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2, 3, 4, 5, width=13)
        init_rect_dict['_Rectangle__width'] = 2
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2, 3, 4, 5, height=13)
        init_rect_dict['_Rectangle__height'] = 3
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2, 3, 4, 5, x=13)
        init_rect_dict['_Rectangle__x'] = 4
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(89, 2, 3, 4, 5, y=13)
        init_rect_dict['_Rectangle__y'] = 5
        self.assertEqual(rect1.__dict__, init_rect_dict)

    def test_Rectangle_d0(self):
        """ Testing update method (kwargs): using kwargs only """

        rect1 = Rectangle(10, 10, 10, 10)
        init_rect_dict = rect1.__dict__
        rect1.update(id=1)
        init_rect_dict['id'] = 10
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(width=2)
        init_rect_dict['_Rectangle__width'] = 2
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(height=3)
        init_rect_dict['_Rectangle__height'] = 3
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(x=4)
        init_rect_dict['_Rectangle__x'] = 4
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(y=5)
        init_rect_dict['_Rectangle__y'] = 5
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(id=11, width=12, height=13, x=14, y=15)
        self.assertEqual(rect1.id, 11)
        self.assertEqual(rect1.width, 12)
        self.assertEqual(rect1.height, 13)
        self.assertEqual(rect1.x, 14)
        self.assertEqual(rect1.y, 15)
        rect1.update(height=11, y=12, width=13, id=14, x=15)
        self.assertEqual(rect1.id, 14)
        self.assertEqual(rect1.width, 13)
        self.assertEqual(rect1.height, 11)
        self.assertEqual(rect1.x, 15)
        self.assertEqual(rect1.y, 12)

    def test_Rectangle_d1(self):
        """ Testing update method (kwargs): using kwargs and args together """

        rect1 = Rectangle(10, 10, 10, 10)
        init_rect_dict = rect1.__dict__
        rect1.update(13, width=2)
        init_rect_dict['id'] = 13
        init_rect_dict['_Rectangle__width'] = 2
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(13, 2, height=3)
        init_rect_dict['_Rectangle__height'] = 3
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(13, 2, 3, x=4)
        init_rect_dict['_Rectangle__x'] = 4
        self.assertEqual(rect1.__dict__, init_rect_dict)
        rect1.update(13, 2, 3, 4, y=5)
        init_rect_dict['_Rectangle__y'] = 5
        self.assertEqual(rect1.__dict__, init_rect_dict)

    def test_Rectangle_d2(self):
        """ Testing update method (kwargs): passing bad keys """

        rect1 = Rectangle(10, 10, 10, 10)
        init_rect_dict = rect1.__dict__
        rect1.update(13, blah=2)
        init_rect_dict['id'] = 13
        self.assertEqual(rect1.__dict__, init_rect_dict)

    def test_Rectangle_d3(self):
        """ Testing to_dictionary method: without self argument """

        with self.assertRaises(TypeError) as excpt:
            Rectangle.to_dictionary()
        excpt_msg = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Rectangle_d4(self):
        """ Testing to_dictionary method: without self argument """

        rect1 = Rectangle(10, 2, 1, 9)
        my_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(rect1.to_dictionary(), my_dict)
        rect2 = Rectangle(1, 1)
        rect2.update(**rect1.to_dictionary())
        self.assertEqual(rect2.to_dictionary(), my_dict)

if __name__ == '__main__':
    unittest.main()
