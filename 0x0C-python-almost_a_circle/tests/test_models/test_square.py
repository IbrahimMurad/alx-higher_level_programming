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

    def test_Square_c0(self):
        """ Testing display method: with only width and height """

        my_rect = Rectangle(1,1)
        with self.assertRaises(TypeError) as excpt:
            Square.display()
        excpt_msg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_c1(self):
        """ Testing display method: with only width and height
        x = 0 and y = 0 """

        my_sqr = Square(1)
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
        my_out = "#\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_sqr.size = 5
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
        my_out = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_sqr.size = 10
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
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

    def test_Square_c2(self):
        """ Testing display method: x and y included """

        my_sqr = Square(1, 1, 1)
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
        my_out = "\n #\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_sqr.size = 5
        my_sqr.x = 0
        my_sqr.y = 5
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
        my_out = "\n\n\n\n\n#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_sqr.x = 5
        my_sqr.y = 0
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
        my_out = "     #####\n     #####\n     #####\n     #####\n     #####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_sqr.x = 3
        my_sqr.y = 3
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
        my_out = "\n\n\n   #####\n   #####\n   #####\n   #####\n   #####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

        my_sqr.x = 18
        my_sqr.y = 10
        my_IO = io.StringIO()
        with redirect_stdout(my_IO):
            my_sqr.display()
        my_out = "\n\n\n\n\n\n\n\n\n\n\
                  #####\n\
                  #####\n\
                  #####\n\
                  #####\n\
                  #####\n"
        self.assertEqual(my_IO.getvalue(), my_out)

    def test_Square_c3(self):
        """ Testing __str__: without passing self """

        my_sqr = Square(1,1, 1, 1)
        with self.assertRaises(TypeError) as excpt:
            Square.__str__()
        excpt_msg = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_c4(self):
        """ Testing __str__: with different attributes values """

        my_sqr = Square(15)
        my_out = "[Square] (1) 0/0 - 15"
        self.assertEqual(str(my_sqr), my_out)

        my_sqr = Square(7,10, 5)
        my_out = "[Square] (2) 10/5 - 7"
        self.assertEqual(str(my_sqr), my_out)

        my_sqr = Square(6, 10, 5, 'superID')
        my_out = "[Square] (superID) 10/5 - 6"
        self.assertEqual(str(my_sqr), my_out)

    def test_Square_c5(self):
        """ Testing update method: without self as an argument """

        with self.assertRaises(TypeError) as excpt:
            Square.update()
        excpt_msg = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_c6(self):
        """ Testing update method (args): with differenct values """

        sqr1 = Square(10, 10, 10)
        init_sqr_dict = sqr1.__dict__
        sqr1.update(89)
        init_sqr_dict['id'] = 89
        self.assertEqual(sqr1.__dict__, init_sqr_dict)
        sqr1.update(89, 2)
        init_sqr_dict['_Rectangle__width'] = 2
        init_sqr_dict['_Rectangle__height'] = 2
        self.assertEqual(sqr1.__dict__, init_sqr_dict)
        sqr1.update(89, 2, 4)
        init_sqr_dict['_Rectangle__x'] = 4
        self.assertEqual(sqr1.__dict__, init_sqr_dict)
        sqr1.update(89, 2, 4, 5)
        init_sqr_dict['_Rectangle__y'] = 5
        self.assertEqual(sqr1.__dict__, init_sqr_dict)

    def test_Square_c7(self):
        """ Testing update method (args): with bad values """

        sqr1 = Square(10, 10, 10)

        with self.assertRaises(TypeError) as excpt:
            sqr1.update(10, '1')
        excpt_msg = "width must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

        with self.assertRaises(TypeError) as excpt:
            sqr1.update(10, 3, '4')
        excpt_msg = "x must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

        with self.assertRaises(TypeError) as excpt:
            sqr1.update(89, 3, 4, '5')
        excpt_msg = "y must be an integer"
        self.assertEqual(str(excpt.exception), excpt_msg)

        rect1 = Rectangle(10, 10, 10, 10)

        with self.assertRaises(ValueError) as excpt:
            sqr1.update(10, -3)
        excpt_msg = "width must be > 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

        with self.assertRaises(ValueError) as excpt:
            sqr1.update(10, 3, -4)
        excpt_msg = "x must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

        with self.assertRaises(ValueError) as excpt:
            sqr1.update(89, 3, 4, -5)
        excpt_msg = "y must be >= 0"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_c8(self):
        """ Testing update method (kwargs): skipping kwargs """

        sqr1 = Square(10, 10, 10)
        sqr1.update(89, 5, 4, 5, id=13)
        self.assertEqual(str(sqr1), "[Square] (89) 4/5 - 5")
        sqr1.update(89, 5, 4, 5, size=13)
        self.assertEqual(str(sqr1), "[Square] (89) 4/5 - 5")
        sqr1.update(89, 5, 4, 5, x=13)
        self.assertEqual(str(sqr1), "[Square] (89) 4/5 - 5")
        sqr1.update(89, 5, 4, 5, y=13)
        self.assertEqual(str(sqr1), "[Square] (89) 4/5 - 5")

    def test_Square_c9(self):
        """ Testing update method (kwargs): using kwargs only """

        sqr1 = Square(10, 10, 10)
        self.assertEqual(str(sqr1), "[Square] (1) 10/10 - 10")
        sqr1.update(id=99)
        self.assertEqual(str(sqr1), "[Square] (99) 10/10 - 10")
        sqr1.update(size=2)
        self.assertEqual(str(sqr1), "[Square] (99) 10/10 - 2")
        sqr1.update(x=4)
        self.assertEqual(str(sqr1), "[Square] (99) 4/10 - 2")
        sqr1.update(y=5)
        self.assertEqual(str(sqr1), "[Square] (99) 4/5 - 2")
        sqr1.update(id=11, size=13, x=14, y=15)
        self.assertEqual(str(sqr1), "[Square] (11) 14/15 - 13")
        sqr1.update(y=12, size=13, id=14, x=15)
        self.assertEqual(str(sqr1), "[Square] (14) 15/12 - 13")

    def test_Square_d1(self):
        """ Testing update method (kwargs): passing bad keys """

        sqr1 = Square(10, 10, 10)
        self.assertEqual(str(sqr1), "[Square] (1) 10/10 - 10")
        sqr1.update(13, blah=2)
        self.assertEqual(str(sqr1), "[Square] (13) 10/10 - 10")
        

    def test_Square_d2(self):
        """ Testing to_dictionary method: without self argument """

        with self.assertRaises(TypeError) as excpt:
            Square.to_dictionary()
        excpt_msg = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_Square_d2(self):
        """ Testing to_dictionary method: without self argument """

        sqr1 = Square(10, 11, 9)
        my_dict = {'id': 1, 'size': 10, 'x': 11, 'y': 9}
        self.assertEqual(sqr1.to_dictionary(), my_dict)
        sqr2 = Square(1)
        sqr2.update(**sqr1.to_dictionary())
        self.assertEqual(sqr2.to_dictionary(), my_dict)

if __name__ == '__main__':
    unittest.main()
