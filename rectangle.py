import unittest

def area(a, b):
    ##Принимает числа a, b. Возвращает произведение чисел a, b
    ##Accepts numbers a and b. Returns the product of numbers a and b
    return a*b

def perimeter(a, b):
    ##Принимает числа a, b. Возвращает сумму произведения чисел a, b на 2
    ##Accepts numbers a and b. Returns the sum of the product of numbers a and b multiplied by 2
    return 2*a + 2*b


class RectangleTestCase(unittest.TestCase):
   def test_area1(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_area2(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_per1(self):
       res = perimeter(0, 0)
       self.assertEqual(res, 0)
       
   def test_per2(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)