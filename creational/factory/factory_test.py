import unittest
from unittest import TestCase
from factory import IShape, Circle, Square, Rectangle, ShapeFactory


class AbstractShapeTest(TestCase):
    ''' Check instantiation of abstract shape class '''

    def test_abstract_instantiation_error(self):
        with self.assertRaises(TypeError) as cm:
            instance = IShape()

        msg = "Can't instantiate abstract class IShape with abstract method draw"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance_error(self):
        class NewClass(IShape):
            pass

        with self.assertRaises(TypeError) as cm:
            instance = NewClass()

        msg = "Can't instantiate abstract class NewClass with abstract method draw"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance(self):
        class NewClass(IShape):
            def draw(self):
                pass

        instance = NewClass()

        self.assertIsInstance(instance, NewClass)
        self.assertIsInstance(instance, IShape)


class ConcreteShapeTest(TestCase):
    ''' Check instantiation of concrete shape classes '''

    def test_circle_instantiation(self):
        shape = ShapeFactory.getShape('circle')
        shape.draw()

        self.assertIsInstance(shape, Circle)
        self.assertIsInstance(shape, IShape)

    def test_square_instantiation(self):
        shape = ShapeFactory.getShape('square')
        shape.draw()

        self.assertIsInstance(shape, Square)
        self.assertIsInstance(shape, IShape)

    def test_rectangle_instantiation(self):
        shape = ShapeFactory.getShape('rectangle')
        shape.draw()

        self.assertIsInstance(shape, Rectangle)
        self.assertIsInstance(shape, IShape)


if __name__ == '__main__':
    unittest.main()
