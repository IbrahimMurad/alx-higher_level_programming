import unittest
from models.base import Base

class TestBase(unittest.TestCase):
     
    # testing __init__
    def test_Base_1(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
    
    def test_Base_2(self):
        base1 = Base()
        self.assertEqual(base1.id, 2)
    
    def test_Base_3(self):
        base1 = Base()
        self.assertEqual(base1.id, 3)
    
    def test_Base_4(self):
        base1 = Base(12)
        self.assertEqual(base1.id, 12)
        
    def test_Base_5(self):
        base1 = Base()
        self.assertEqual(base1.id, 4)


if __name__ == '__main__':
    unittest.main()