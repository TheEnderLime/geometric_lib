import unittest

def area(a, h):
    ##Принимает числа a, h. Возвращает их произведение делённое на 2
    ##Takes the numbers a and h. Returns their product divided by 2
    return a * h / 2

def perimeter(a, b , c):
    ##Принимает числа a, b, c. Возвращает их сумму
    ##Accepts the numbers a, b, and c. Returns their sum
    return a + b + c

class RectangleTestCase(unittest.TestCase):
   def test_area1(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_area2(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_per1(self):
       res = perimeter(0, 0, 0)
       self.assertEqual(res, 0)

   def test_per2(self):
       res = perimeter(10, 10, 10)
       self.assertEqual(res, 30)