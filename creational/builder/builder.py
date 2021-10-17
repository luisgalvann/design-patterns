from abc import ABC, abstractstaticmethod


class Vehicle:
    ''' Product class implementation '''

    def __init__(self):
        self.vtype = None
        self.wheels = None

    def run(self) -> str:
        return f'The {self.vtype} is running'


class IVehicleBuilder(ABC):
    ''' Abstract builder «interface» implementation '''

    @abstractstaticmethod
    def __init__() -> None:
        raise NotImplementedError

    @abstractstaticmethod
    def set_vtype() -> None:
        raise NotImplementedError

    @abstractstaticmethod
    def set_wheels() -> None:
        raise NotImplementedError

    @abstractstaticmethod
    def get_vehicle() -> None:
        raise NotImplementedError


class BikeBuilder(IVehicleBuilder):
    ''' Concrete bike builder class implementation '''

    def __init__(self) -> None:
        self.vehicle = Vehicle()

    def set_vtype(self) -> None:
        self.vehicle.vtype = 'bike'

    def set_wheels(self) -> None:
        self.vehicle.wheels = 2

    def get_vehicle(self) -> Vehicle:
        return self.vehicle


class CarBuilder(IVehicleBuilder):
    ''' Concrete car builder class implementation '''

    def __init__(self) -> None:
        self.vehicle = Vehicle()

    def set_vtype(self) -> None:
        self.vehicle.vtype = 'car'

    def set_wheels(self) -> None:
        self.vehicle.wheels = 4

    def get_vehicle(self) -> Vehicle:
        return self.vehicle


class Engineer:
    ''' Director class implementation '''

    @staticmethod
    def construct(vtype: str) -> Vehicle:
        builder = {
            'bike': BikeBuilder(),
            'car': CarBuilder()
        }.get(vtype)

        builder.set_vtype()
        builder.set_wheels()
        vehicle = builder.get_vehicle()

        return vehicle
