import unittest
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
     
    """ testing __init__ """
    
    # passing: width and height
    def test_Rectangle_a1(self):
        Rect1 = Rectangle(7, 9)
        self.assertEqual(Rect1.id, 5)
        self.assertEqual(Rect1.width, 7)
        self.assertEqual(Rect1.height, 9)
        self.assertEqual(Rect1.x, 0)
        self.assertEqual(Rect1.y, 0)
    
    # passing only width, height and x
    def test_Rectangle_a2(self):
        Rect2 = Rectangle(7, 9, 4)
        self.assertEqual(Rect2.id, 6)
        self.assertEqual(Rect2.width, 7)
        self.assertEqual(Rect2.height, 9)
        self.assertEqual(Rect2.x, 4)
        self.assertEqual(Rect2.y, 0)
    
    # passing only width, height x, and y
    def test_Rectangle_a3(self):
        Rect3 = Rectangle(7, 9, 4, 3)
        self.assertEqual(Rect3.id, 7)
        self.assertEqual(Rect3.width, 7)
        self.assertEqual(Rect3.height, 9)
        self.assertEqual(Rect3.x, 4)
        self.assertEqual(Rect3.y, 3)
    
    # passing only width, height x, y and id
    def test_Rectangle_a4(self):
        Rect4 = Rectangle(7, 9, 4, 3, 11)
        self.assertEqual(Rect4.id, 11)
        self.assertEqual(Rect4.width, 7)
        self.assertEqual(Rect4.height, 9)
        self.assertEqual(Rect4.x, 4)
        self.assertEqual(Rect4.y, 3)
    
    """ test attributes validation, by checking the rased error type
    and the raised message """
    
    # passing width as float once then,
    # passing it as string
    def test_Rectangle_b1(self):
        with self.assertRaises(TypeError) as excpt:
            Rect5 = Rectangle(7.0, 9, 1, 1, 3)
        self.assertEqual(str(excpt.exception), "width must be an integer")
        with self.assertRaises(TypeError) as excpt:
            Rect6 = Rectangle('7', 9, 1, 1, 3)
        self.assertEqual(str(excpt.exception), "width must be an integer")
    
    # passing height as float once then,
    # passing it as string
    def test_Rectangle_b2(self):
        with self.assertRaises(TypeError) as excpt:
            Rect7 = Rectangle(7, 9.0, 1, 1, 3)
        self.assertEqual(str(excpt.exception), "height must be an integer")
        with self.assertRaises(TypeError) as excpt:
            Rect8 = Rectangle(7, '9', 1, 1, 3)
        self.assertEqual(str(excpt.exception), "height must be an integer")

    # passing x as float once then,
    # passing it as string
    def test_Rectangle_b3(self):
        with self.assertRaises(TypeError) as excpt:
            Rect9 = Rectangle(7, 9, 1.0, 1, 3)
        self.assertEqual(str(excpt.exception), "x must be an integer")
        with self.assertRaises(TypeError) as excpt:
            Rect10 = Rectangle(7, 9, '1', 1, 3)
        self.assertEqual(str(excpt.exception), "x must be an integer")

    # passing y as float once then,
    # passing it as string
    def test_Rectangle_b4(self):
        with self.assertRaises(TypeError) as excpt:
            Rect11 = Rectangle(7, 9, 1, 1.0, 3)
        self.assertEqual(str(excpt.exception), "y must be an integer")
        with self.assertRaises(TypeError) as excpt:
            Rect12 = Rectangle(7, 9, 1, '1', 3)
        self.assertEqual(str(excpt.exception), "y must be an integer")

    # passing width equals 0 once then,
    # passing it as a negative number
    def test_Rectangle_b5(self):
        with self.assertRaises(ValueError) as excpt:
            Rect13 = Rectangle(0, 9, 1, 1, 3)
        self.assertEqual(str(excpt.exception), "width must be > 0")
        with self.assertRaises(ValueError) as excpt:
            Rect14 = Rectangle(-2, 9, 1, 1, 3)
        self.assertEqual(str(excpt.exception), "width must be > 0")

    # passing height equals 0 once then,
    # passing it as a negative number
    def test_Rectangle_b6(self):
        with self.assertRaises(ValueError) as excpt:
            Rect15 = Rectangle(7, 0, 1, 2, 3)
        self.assertEqual(str(excpt.exception), "height must be > 0")
        with self.assertRaises(ValueError) as excpt:
            Rect16 = Rectangle(7, -3, 1, 2, 3)
        self.assertEqual(str(excpt.exception), "height must be > 0")

    # passing x as a negative number
    def test_Rectangle_b7(self):
        with self.assertRaises(ValueError) as excpt:
            Rect17 = Rectangle(7, 9, -3, 1, 3)
        self.assertEqual(str(excpt.exception), "x must be >= 0")
    
    # passing y as a negative number
    def test_Rectangle_b8(self):
        with self.assertRaises(ValueError) as excpt:
            Rect18 = Rectangle(7, 9, 1, -10, 3)
        self.assertEqual(str(excpt.exception), "y must be >= 0")
    
    # initializing with zero argument
    def test_Rectangle_b9(self):
        with self.assertRaises(TypeError):
            rect19 = Rectangle()
    
    # initializing with one argument
    def test_Rectangle_91(self):
        with self.assertRaises(TypeError):
            rect19 = Rectangle(7)

    """ test area method """
    
    # normal and large numbers
    def test_Rectangle_c1(self):
        rect20 = Rectangle(3, 2)
        self.assertEqual(rect20.area(), 6)
        rect21 = Rectangle(20, 10)
        self.assertEqual(rect21.area(), 200)


    """ test display method """
    
    # normal and large numbers
    def test_Rectangle_d1(self):
        rect22 = Rectangle(3, 2)
        self.assertEqual(rect22.display(), 6)
        rect23 = Rectangle(20, 10)
        self.assertEqual(rect23.area(), 200)

if __name__ == '__main__':
    unittest.main()
