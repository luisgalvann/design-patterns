import unittest
from unittest import TestCase
from class_adapter import (
    HexadecimalSystem, IDecimalSystem, 
    HexDecAdapter, AvgCalculator)


class AbstractSystemTest(TestCase):
    ''' Test instantiation of abstract class '''

    def test_abstract_instantiation_error(self):
        with self.assertRaises(TypeError) as cm:
            instance = IDecimalSystem()

        msg = "Can't instantiate abstract class IDecimalSystem with abstract "\
              "methods get_max_dec, get_min_dec"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance_error(self):
        class NewClass(IDecimalSystem):
            pass

        with self.assertRaises(TypeError) as cm:
            instance = NewClass()

        msg = "Can't instantiate abstract class NewClass with abstract "\
              "methods get_max_dec, get_min_dec"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance(self):
        class NewClass(IDecimalSystem):
            def get_min_dec(self):
                pass

            def get_max_dec(self):
                pass

        instance = NewClass()

        self.assertIsInstance(instance, NewClass)
        self.assertIsInstance(instance, IDecimalSystem)


class AdapteeSystemTest(TestCase):
    ''' Test instantiation and methods of adaptee class '''

    def test_system_instantiation(self):
        system = HexadecimalSystem()
        
        self.assertIsInstance(system, HexadecimalSystem)

    def test_system_methods(self):
        system = HexadecimalSystem()
        result_a = system.get_min_hex()
        result_b = system.get_max_hex()

        self.assertIsInstance(result_a, str)
        self.assertIsInstance(result_b, str)


class AdapterSystemTest(TestCase):
    ''' Test instantiation and methods of adapter class '''

    def test_system_instantiation(self):
        system = HexDecAdapter()
        
        self.assertIsInstance(system, HexadecimalSystem)
        self.assertIsInstance(system, IDecimalSystem)
        self.assertIsInstance(system, HexDecAdapter)

    def test_system_methods(self):
        system = HexDecAdapter()
        result_a = system.get_min_dec()
        result_b = system.get_max_dec()

        self.assertIsInstance(result_a, int)
        self.assertIsInstance(result_b, int)


class ClientTest(TestCase):
    ''' Test instantiation and methods of client class '''

    def test_client_instantiation(self):
        client = AvgCalculator()
        
        self.assertIsInstance(client, AvgCalculator)

    def test_client_adapter(self):
        client = AvgCalculator()
        adapter = client.system

        self.assertIsInstance(adapter, HexadecimalSystem)
        self.assertIsInstance(adapter, IDecimalSystem)
        self.assertIsInstance(adapter, HexDecAdapter)

    def test_client_method(self):
        client = AvgCalculator()
        result = client.get_avg_dec()

        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()
