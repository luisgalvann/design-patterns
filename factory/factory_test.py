import unittest
from unittest import TestCase
from factory import Shape, Circle, Square, Rectangle, ShapeFactory


class AbstractShapeTest(TestCase):
    ''' Check instantiation of abstract class '''

    def test_abstract_instantiation_error(self):
        with self.assertRaises(TypeError) as cm:
            instance = Shape()

        msg = "Can't instantiate abstract class Shape with abstract method draw"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance_error(self):
        class NewClass(Shape):
            pass

        with self.assertRaises(TypeError) as cm:
            instance = NewClass()

        msg = "Can't instantiate abstract class NewClass with abstract method draw"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance(self):
        class NewClass(Shape):
            def draw(self):
                pass

        instance = NewClass()

        self.assertIsInstance(instance, NewClass)
        self.assertIsInstance(instance, Shape)


class ConcreteShapesTest(TestCase):
    ''' Check instantiation of concrete classes '''

    def test_circle_instantiation(self):
        shape = ShapeFactory.getShape('circle')
        shape.draw()

        assert isinstance(shape, Circle)
        assert isinstance(shape, Shape)

    def test_square_instantiation(self):
        shape = ShapeFactory.getShape('square')
        shape.draw()

        assert isinstance(shape, Square)
        assert isinstance(shape, Shape)

    def test_rectangle_instantiation(self):
        shape = ShapeFactory.getShape('rectangle')
        shape.draw()

        assert isinstance(shape, Rectangle)
        assert isinstance(shape, Shape)


if __name__ == '__main__':
    unittest.main()
