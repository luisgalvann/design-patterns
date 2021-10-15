import unittest
from unittest import TestCase
import time
from singleton import Singleton


class SingletonTest(TestCase):
    ''' Test instantiation and method of singleton class '''

    def test_singleton_instantiation(self):
        first_instance = Singleton()
        second_instance = Singleton()

        self.assertEqual(first_instance, second_instance)

    def test_singleton_creation_time(self):
        first_instance = Singleton()
        time.sleep(2)
        second_instance = Singleton()

        first_time = first_instance.get_creation_time()
        second_time = second_instance.get_creation_time()

        self.assertEqual(first_time, second_time)


if __name__ == '__main__':
    unittest.main()
