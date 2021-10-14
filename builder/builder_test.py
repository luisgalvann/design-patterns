import unittest
from unittest import TestCase
from builder import Vehicle, IVehicleBuilder, BikeBuilder, CarBuilder, Engineer


class AbstractBuilderTest(TestCase):
    ''' Check instantiation of abstract builder class '''

    def test_abstract_instantiation_error(self):
        with self.assertRaises(TypeError) as cm:
            instance = IVehicleBuilder()

        msg = "Can't instantiate abstract class IVehicleBuilder "\
              "with abstract methods get_vehicle, set_vtype, set_wheels"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance_error(self):
        class NewClass(IVehicleBuilder):
            pass

        with self.assertRaises(TypeError) as cm:
            instance = NewClass()

        msg = "Can't instantiate abstract class NewClass "\
              "with abstract methods get_vehicle, set_vtype, set_wheels"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance(self):
        class NewClass(IVehicleBuilder):
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
    ''' Check instantiation of concrete builder classes '''

    def test_bike_builder(self):
        builder = BikeBuilder()
        builder.set_vtype()
        builder.set_wheels()
        vehicle = builder.get_vehicle()

        self.assertIsInstance(builder, BikeBuilder)
        self.assertIsInstance(builder, IVehicleBuilder)

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'Bike')
        self.assertEqual(vehicle.wheels, 2)


    def test_car_builder(self):
        builder = CarBuilder()
        builder.set_vtype()
        builder.set_wheels()
        vehicle = builder.get_vehicle()

        self.assertIsInstance(builder, CarBuilder)
        self.assertIsInstance(builder, IVehicleBuilder)

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'Car')
        self.assertEqual(vehicle.wheels, 4)


class ProductTest(TestCase):
    ''' Check instantiation of product class '''

    def test_bike_instantiation(self):
        vehicle = Vehicle()
        vehicle.vtype = 'Bike'
        result = vehicle.run()

        msg = 'The Bike is running'
        self.assertEqual(result, msg)

    def test_car_instantiation(self):
        vehicle = Vehicle()
        vehicle.vtype = 'Car'
        result = vehicle.run()

        msg = 'The Car is running'
        self.assertEqual(result, msg)


class DirectorTest(TestCase):
    ''' Check instantiation of product class '''

    def test_engineer_bike_construction(self):
        vehicle = Engineer.construct('Bike')

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'Bike')
        self.assertEqual(vehicle.wheels, 2)

    def test_engineer_car_construction(self):
        vehicle = Engineer.construct('Car')

        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle.vtype, 'Car')
        self.assertEqual(vehicle.wheels, 4)


if __name__ == '__main__':
    unittest.main()
