from datetime import datetime


# The Singleton class can be implemented in different ways. 
# Some methods include: metaclass, base class or decorator.


class SingletonMeta(type):
    ''' Singleton metaclass implementation '''

    _instance = None

    def __call__(self, *args, **kwargs) -> SingletonMeta:
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)

        return self._instance


class Singleton(metaclass=SingletonMeta):
    ''' Singleton class implementation '''

    def __init__(self) -> None:
        self.creation_time = datetime.now()

    def get_creation_time(self) -> datetime:
        return self.creation_time
