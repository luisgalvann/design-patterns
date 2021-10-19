import unittest
from unittest import TestCase
from command import (
    ICommand, SwitchOnCommand, 
    SwitchOffCommand, Light, Switch)


class AbstractCommandTest(TestCase):
    ''' Test instantiation of abstract command class '''

    def test_abstract_instantiation_error(self):
        with self.assertRaises(TypeError) as cm:
            instance = ICommand()

        msg = "Can't instantiate abstract class ICommand with " \
              "abstract methods __init__, execute"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance_error(self):
        class NewClass(ICommand):
            pass

        with self.assertRaises(TypeError) as cm:
            instance = NewClass()

        msg = "Can't instantiate abstract class NewClass with " \
              "abstract methods __init__, execute"
        self.assertEqual(msg, str(cm.exception))

    def test_abstract_inheritance(self):
        class NewClass(ICommand):
            def __init__(self):
                pass
            def execute(self):
                pass

        instance = NewClass()

        self.assertIsInstance(instance, NewClass)
        self.assertIsInstance(instance, ICommand)


class ReceiverTest(TestCase):
    ''' Test instantiation and methods of receiver class '''

    def test_light_instantiation(self):
        receiver = Light()

        self.assertIsInstance(receiver, Light)

    def test_light_methods(self):
        receiver = Light()
        result_on = receiver.turn_on()
        result_off = receiver.turn_off()

        self.assertEqual(result_on, 'Light turned ON')
        self.assertEqual(result_off, 'Light turned OFF')


class ConcreteCommandTest(TestCase):
    ''' Test instantiation of concrete command classes '''

    def test_switch_on_instantiation(self):
        receiver = Light()
        command = SwitchOnCommand(receiver)
        result = command.execute()

        self.assertIsInstance(command, SwitchOnCommand)
        self.assertIsInstance(command, ICommand)
        self.assertIsInstance(command.receiver, Light)
        self.assertEqual(result, 'Light turned ON')

    def test_switch_off_instantiation(self):
        receiver = Light()
        command = SwitchOffCommand(receiver)
        result = command.execute()

        self.assertIsInstance(command, SwitchOffCommand)
        self.assertIsInstance(command, ICommand)
        self.assertIsInstance(command.receiver, Light)
        self.assertEqual(result, 'Light turned OFF')


class InvokerTest(TestCase):
    ''' Test instantiation and methods of invoker class '''

    def test_switch_instantiation(self):
        invoker = Switch()

        self.assertIsInstance(invoker, Switch)
        self.assertIsInstance(invoker.commands, dict)
        self.assertIsInstance(invoker.history, list)

    def test_switch_register_method(self):
        invoker = Switch()
        receiver = Light()

        command_on = SwitchOnCommand(receiver)
        command_off = SwitchOffCommand(receiver)

        cname_on = 'switch on light'
        cname_off = 'switch off light'

        invoker.register(cname_on, command_on)
        invoker.register(cname_off, command_off)

        self.assertIn(cname_on, invoker.commands)
        self.assertIn(cname_off, invoker.commands)
        self.assertEqual(invoker.commands[cname_on], command_on)
        self.assertEqual(invoker.commands[cname_off], command_off)

    def test_switch_execute_method(self):
        invoker = Switch()
        receiver = Light()

        command_on = SwitchOnCommand(receiver)
        command_off = SwitchOffCommand(receiver)

        cname_on = 'switch on light'
        cname_off = 'switch off light'

        invoker.register(cname_on, command_on)
        invoker.register(cname_off, command_off)

        result_on = invoker.execute(cname_on)
        result_off = invoker.execute(cname_off)


        self.assertEqual(result_on, 'Light turned ON')
        self.assertEqual(result_off, 'Light turned OFF')


if __name__ == '__main__':
    unittest.main()
