from abc import ABC, abstractstaticmethod
from datetime import datetime
from typing import Any, List, Dict


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

    def __init__(self, receiver: Any) -> None:
        self.receiver = receiver

    def execute(self) -> str:
        result = self.receiver.turn_on()
        return result


class SwitchOffCommand(ICommand):
    ''' Concrete «switch off» command implementation '''

    def __init__(self, receiver: Any) -> None:
        self.receiver = receiver

    def execute(self) -> str:
        result = self.receiver.turn_off()
        return result


class Light:
    ''' Receiver class implementation '''

    def turn_on(self) -> str:
        return 'Light turned ON'

    def turn_off(self) -> str:
        return 'Light turned OFF'


class Switch:
    ''' Invoker class implementation '''

    def __init__(self) -> None:
        self.commands: Dict[str, ICommand] = {}
        self.history: List[tuple] = []

    def register(self, cname: str, command: ICommand) -> None:
        self.commands[cname] = command

    def execute(self, cname: str) -> None:
        if cname in self.commands.keys():
            result = self.commands[cname].execute()
            self.history.append((datetime.now(), cname))
            return result

    def get_history(self) -> None:
        for ctime, cname in self.history:
            print(ctime.strftime('%H:%M:%S'), cname)
