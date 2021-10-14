from datetime import datetime


class SingletonMeta(type):
    ''' The Singleton class can be implemented in different ways. 
    Some methods include: metaclass, base class or decorator '''

    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)

        return self._instance


class Singleton(metaclass=SingletonMeta):
    ''' Singleton Implementation '''

    def __init__(self):
        self.creation_time = datetime.now()

    def get_creation_time(self):
        return self.creation_time
