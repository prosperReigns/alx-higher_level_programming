import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Testbase(unittest.TestCase):
    def setUp(self):
        self.base = Base()
        self.rectangle = Rectangle(5, 7, 5, 5)
        self.square = Square(5, 5, 5)

    # def test_base_id(self):
    #     id = self.base.id
    #     self.assertEqual(id, 1)

    # def test_rectangle_id(self):
    #     id = self.rectangle.id
    #     self.assertEqual(id, 5)

    # def test_square_id(self):
    #     id = self.square.id
    #     self.assertEqual(id, 9)

    def test_rectangle_dimension_for_integer(self):
        width = self.rectangle.width
        self.assertEqual(width, 5)

        height = self.rectangle.height
        self.assertEqual(height, 7)

        x = self.rectangle.x
        self.assertEqual(x, 5)

        y = self.rectangle.y
        self.assertEqual(y, 5)


    def test_rectangle_dimension_for_string_value(self):
        self.assertRaises(TypeError, self.rectangle.width, "hello")
        self.assertRaises(TypeError, self.rectangle.height, "hello")
        self.assertRaises(TypeError, self.rectangle.x, "hello")
        self.assertRaises(TypeError, self.rectangle.y, "hello")
       

    def test_rectangle_dimension_for_negative_values(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = -7

        with self.assertRaises(ValueError):
            self.rectangle.height = -7
        
        with self.assertRaises(ValueError):
            self.rectangle.x = -7

        with self.assertRaises(ValueError):
            self.rectangle.y = -7


    def test_rectangle_dimension_for_float(self):
        self.assertRaises(TypeError, self.rectangle.width, 34.5)
        self.assertRaises(TypeError, self.rectangle.height, 12.25)
        self.assertRaises(TypeError, self.rectangle.x, 11.02)
        self.assertRaises(TypeError, self.rectangle.y, 6.5)

    def test_rectangle_dimension_for_string_number(self):
        pass

    def test_rectangle_area(self):
        area = self.rectangle.area()
        self.assertEqual(area, 35)






















if __name__ == "__main__":
    unittest.main()