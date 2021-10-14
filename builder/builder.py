from abc import ABC, abstractmethod


class Vehicle:
    ''' Product class implementation '''

    def __init__(self):
        self.vtype = None
        self.wheels = None

    def run(self) -> str:
        return f'The {self.vtype} is running'


class IVehicleBuilder(ABC):
    ''' Abstract Builder «interface» '''

    @staticmethod
    @abstractmethod
    def set_vtype() -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def set_wheels() -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_vehicle() -> None:
        raise NotImplementedError


class BikeBuilder(IVehicleBuilder):
    ''' Concrete Bike Builder '''

    def __init__(self) -> None:
        self.vehicle = Vehicle()

    def set_vtype(self) -> None:
        self.vehicle.vtype = 'Bike'

    def set_wheels(self) -> None:
        self.vehicle.wheels = 2

    def get_vehicle(self) -> Vehicle:
        return self.vehicle


class CarBuilder(IVehicleBuilder):
    ''' Concrete Car Builder '''

    def __init__(self) -> None:
        self.vehicle = Vehicle()

    def set_vtype(self) -> None:
        self.vehicle.vtype = 'Car'

    def set_wheels(self) -> None:
        self.vehicle.wheels = 4

    def get_vehicle(self) -> Vehicle:
        return self.vehicle


class Engineer:
    ''' Director class implementation '''

    @staticmethod
    def construct(vtype: str) -> Vehicle:
        builder = {
            'Bike': BikeBuilder(),
            'Car': CarBuilder()
        }.get(vtype)

        builder.set_vtype()
        builder.set_wheels()
        vehicle = builder.get_vehicle()

        return vehicle
