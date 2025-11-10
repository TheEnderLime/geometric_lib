import unittest

def area(a):
    ##Принимает число a. Возвращает его квадрат
    ##Takes the number a. Returns its square
    return a * a


def perimeter(a):
    ##Принимает число a. Возвращает его произведение с 4
    ##Accepts a number a. Returns its product with 4
    return 4 * a

class RectangleTestCase(unittest.TestCase):
   def test_area1(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_area2(self):
       res = area(10)
       self.assertEqual(res, 100)
    
   def test_per1(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

   def test_per2(self):
       res = perimeter(10)
       self.assertEqual(res, 40)