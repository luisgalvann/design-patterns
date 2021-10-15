import unittest
from unittest import TestCase
from builder import Vehicle, IVehicleBuilder, BikeBuilder, CarBuilder, Engineer


class AbstractBuilderTest(TestCase):
    ''' Test instantiation of abstract builder class '''

    def test_abstract_instantiation_error(self):
        with self.assertRaises(TypeError) as cm:
            instance = IVehicleBuilder()

        msg = "Can't instantiate abstract class IVehicleBuilder with abstract "\
              "methods __init__, get_vehicle, set_vtype, set_wheels"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance_error(self):
        class NewClass(IVehicleBuilder):
            pass

        with self.assertRaises(TypeError) as cm:
            instance = NewClass()

        msg = "Can't instantiate abstract class NewClass with abstract "\
              "methods __init__, get_vehicle, set_vtype, set_wheels"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance(self):
        class NewClass(IVehicleBuilder):
            def __init__(self):
                pass

            def set_vtype(self):
                pass

            def set_wheels(self):
                pass

            def get_vehicle(self):
                pass

        instance = NewClass()

        self.assertIsInstance(instance, NewClass)
        self.assertIsInstance(instance, IVehicleBuilder)


class ConcreteBuilderTest(TestCase):
    ''' Test instantiation and methods of concrete builder classes '''

    def test_bike_builder(self):
        builder = BikeBuilder()
        builder.set_vtype()
        builder.set_wheels()
        vehicle = builder.get_vehicle()

        self.assertIsInstance(builder, BikeBuilder)
        self.assertIsInstance(builder, IVehicleBuilder)

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'bike')
        self.assertEqual(vehicle.wheels, 2)


    def test_car_builder(self):
        builder = CarBuilder()
        builder.set_vtype()
        builder.set_wheels()
        vehicle = builder.get_vehicle()

        self.assertIsInstance(builder, CarBuilder)
        self.assertIsInstance(builder, IVehicleBuilder)

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'car')
        self.assertEqual(vehicle.wheels, 4)


class ProductTest(TestCase):
    ''' Test instantiation and methods of product class '''

    def test_bike_instantiation(self):
        vehicle = Vehicle()
        vehicle.vtype = 'bike'
        result = vehicle.run()

        msg = 'The bike is running'
        self.assertEqual(result, msg)

    def test_car_instantiation(self):
        vehicle = Vehicle()
        vehicle.vtype = 'car'
        result = vehicle.run()

        msg = 'The car is running'
        self.assertEqual(result, msg)


class DirectorTest(TestCase):
    ''' Test instantiation and methods of director class '''

    def test_engineer_bike_construction(self):
        vehicle = Engineer.construct('bike')

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'bike')
        self.assertEqual(vehicle.wheels, 2)

    def test_engineer_car_construction(self):
        vehicle = Engineer.construct('car')

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'car')
        self.assertEqual(vehicle.wheels, 4)


if __name__ == '__main__':
    unittest.main()
