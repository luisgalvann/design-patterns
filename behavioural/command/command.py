from abc import ABC, abstractstaticmethod
from datetime import datetime


class ICommand(ABC):
    ''' Abstract command «interface» implementation '''

    @abstractstaticmethod
    def __init__() -> None:
        pass

    @abstractstaticmethod
    def execute() -> None:
        pass


class SwitchOnCommand(ICommand):
    ''' Concrete «switch on» command implementation '''

    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.turn_on()


class SwitchOffCommand(ICommand):
    ''' Concrete «switch off» command implementation '''

    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.turn_off()


class Light:
    ''' Receiver class implementation '''

    def turn_on(self) -> None:
        print('Light turned ON')

    def turn_off(self) -> None:
        print('Light turned OFF')


class Switch:
    ''' Invoker class implementation '''

    def __init__(self) -> None:
        self.commands = {}
        self.history = []

    def register(self, cname, command) -> None:
        self.commands[cname] = command

    def execute(self, cname) -> None:
        if cname in self.commands.keys():
            self.commands[cname].execute()
            self.history.append((datetime.now(), cname))

    def get_history(self) -> None:
        for ctime, cname in self.history:
            print(ctime.strftime('%H:%M:%S'), cname)
