from abc import ABC, abstractmethod


class HexSystem:
    ''' Adaptee Implementation '''

    def get_min_hex(self) -> str:
        result = '7D0'
        return result

    def get_max_hex(self) -> str:
        result = '3A98'
        return result

class IDecSystem(ABC):
    ''' Target «interface»  '''

    @staticmethod
    @abstractmethod
    def get_min_dec() -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_max_dec() -> None:
        raise NotImplementedError

class HexDecAdapter(HexSystem, IDecSystem): 
    ''' Adapter Implementation '''

    def get_min_dec(self) -> int:
        result = int(super().get_min_hex(), 16)
        return result

    def get_max_dec(self) -> int:
        result = int(super().get_max_hex(), 16)
        return result


class AvgCalculator:
    ''' Client Implementation '''

    def __init__(self) -> None:
        self.adapter = HexDecAdapter()

    def get_avg_dec(self) -> float:
        a = self.adapter.get_min_dec()
        b = self.adapter.get_max_dec()
        result = (a + b) / 2
        return result
