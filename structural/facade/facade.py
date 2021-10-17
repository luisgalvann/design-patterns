class WashingSystem:
    ''' Subsystem A class implementation '''
 
    def wash(self) -> str:
        return 'A'
 
 
class RinsingSystem:
    ''' Subsystem B class implementation '''
 
    def rinse(self) -> str:
        return 'B'
 
 
class SpinningSystem:
    ''' Subsystem C class implementation '''
 
    def spin(self) -> str:
        return 'C'
 
 
class WashingMachine:
    ''' Facade class implementation '''
 
    def __init__(self) -> None:
        self.washing_system = WashingSystem()
        self.rinsing_system = RinsingSystem()
        self.spinning_system = SpinningSystem()
 
    def start(self) -> str:
        result = self.washing_system.wash()
        result += self.rinsing_system.rinse()
        result += self.spinning_system.spin()

        return result
