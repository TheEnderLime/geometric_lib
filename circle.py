import math
##Импорт библиотеки math, предоставляющая доступ к математическим функциям и константам
##Importing the math library, which provides access to mathematical functions and constants
import unittest

def area(r):
    ##Принимает число r. Возвращает произведение квадрата r и числа pi
    ##Accepts the number r. Returns the product of r squared and pi
    return math.pi * r * r


def perimeter(r):
    ##Принимает число r. Возвращает произведение r и числа pi
    ##Accepts the number r. Returns the product of r and the number pi
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
   def test_area1(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_area2(self):
       res = area(10)
       self.assertEqual(res, 100 * math.pi)

   def test_per1(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
   def test_per2(self):
       res = perimeter(10)
       self.assertEqual(res, 20 * math.pi)