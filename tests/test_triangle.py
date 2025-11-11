import unittest

from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
   def test_area1(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_area2(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

   def test_per1(self):
       res = perimeter(0, 0, 0)
       self.assertEqual(res, 0)

   def test_per2(self):
       res = perimeter(10, 10, 10)
       self.assertEqual(res, 30)