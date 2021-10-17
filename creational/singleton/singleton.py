from datetime import datetime
from typing import Any

# The Singleton class can be implemented in different ways. 
# Some methods include: metaclass, base class or decorator.


class SingletonMeta(type):
    ''' Singleton metaclass implementation '''

    instance: Any = None

    def __call__(self, *args, **kwargs) -> Any:
        if self.instance is None:
            self.instance = super().__call__(*args, **kwargs)

        return self.instance


class Singleton(metaclass=SingletonMeta):
    ''' Singleton class implementation '''

    def __init__(self) -> None:
        self.creation_time = datetime.now()

    def get_creation_time(self) -> datetime:
        return self.creation_time
