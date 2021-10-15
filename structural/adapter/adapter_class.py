from abc import ABC, abstractmethod


class HexadecimalSystem:
    ''' Adaptee Implementation '''

    def get_min_hex(self) -> str:
        result = '7D0'
        return result

    def get_max_hex(self) -> str:
        result = '3A98'
        return result

class IDecimalSystem(ABC):
    ''' Target «interface»  '''

    @staticmethod
    @abstractmethod
    def get_min_dec() -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_max_dec() -> None:
        raise NotImplementedError

class HexDecAdapter(HexadecimalSystem, IDecimalSystem): 
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
        self.system = HexDecAdapter()

    def get_avg_dec(self) -> float:
        a = self.system.get_min_dec()
        b = self.system.get_max_dec()
        result = (a + b) / 2
        return result
