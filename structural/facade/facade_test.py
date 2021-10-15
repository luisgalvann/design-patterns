import unittest
from unittest import TestCase
from facade import WashingSystem, RinsingSystem, SpinningSystem, WashingMachine


class FacadeTest(TestCase):
    ''' Test instantiation and methods of Facade class '''

    def test_facade_instantiation(self):
        facade = WashingMachine()

        self.assertIsInstance(facade, WashingMachine)

    def test_facade_attributes(self):
        facade = WashingMachine()

        self.assertIsInstance(facade.washing_system, WashingSystem)
        self.assertIsInstance(facade.rinsing_system, RinsingSystem)
        self.assertIsInstance(facade.spinning_system, SpinningSystem)

    def test_facade_result(self):
        facade = WashingMachine()
        result = facade.start()

        self.assertEqual(result, 'ABC')


class SubsystemsTest(TestCase):
    ''' Test instantiation and methods of subsystem classes '''

    def test_subsystems_instantiation(self):
        subsystem_a = WashingSystem()
        subsystem_b = RinsingSystem()
        subsystem_c = SpinningSystem()

        self.assertIsInstance(subsystem_a, WashingSystem)
        self.assertIsInstance(subsystem_b, RinsingSystem)
        self.assertIsInstance(subsystem_c, SpinningSystem)

    def test_subsystems_results(self):
        subsystem_a = WashingSystem()
        subsystem_b = RinsingSystem()
        subsystem_c = SpinningSystem()

        result_a = subsystem_a.wash()
        result_b = subsystem_b.rinse()
        result_c = subsystem_c.spin()

        self.assertEqual(result_a, 'A')
        self.assertEqual(result_b, 'B')
        self.assertEqual(result_c, 'C')


if __name__ == '__main__':
    unittest.main()
