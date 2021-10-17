class WashingSystem:
    ''' Subsystem A Class Implementation '''
 
    def wash(self) -> str:
        return 'A'
 
 
class RinsingSystem:
    ''' Subsystem B Class Implementation '''
 
    def rinse(self) -> str:
        return 'B'
 
 
class SpinningSystem:
    ''' Subsystem C Class Implementation '''
 
    def spin(self) -> str:
        return 'C'
 
 
class WashingMachine:
    ''' Facade Class Implementation '''
 
    def __init__(self) -> None:
        self.washing_system = WashingSystem()
        self.rinsing_system = RinsingSystem()
        self.spinning_system = SpinningSystem()
 
    def start(self) -> str:
        result = self.washing_system.wash()
        result += self.rinsing_system.rinse()
        result += self.spinning_system.spin()

        return result
