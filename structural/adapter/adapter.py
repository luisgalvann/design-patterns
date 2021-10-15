from abc import ABC, abstractmethod


class Duck(ABC):
    ''' interface '''
    @abstractmethod
    def quack():
        pass

    @abstractmethod
    def fly():
        pass

class MallardDuck(Duck):
    ''' concrete class '''
    def quack():
        print("Quack")

    def fly():
        print("Fly fly fly!")


class Turkey(ABC):
    ''' interface '''
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    ''' concrete class '''
    def gobble(self):
        print("Gobble gobble..")

    def fly(self):
        print("Flying for a short distance")
  

# Suppose that we are short on Ducks and the solution is to use some
# Turkey objects in their place. we would need to create an adapter

# adaptador con composition
class TurkeyAdapter(Duck):

    def __init__(self, turkey: Turkey):
        self.turkey: Turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


# All that remains is to test our adapter:
duck: MallardDuck = MallardDuck()
turkey: WildTurkey = WildTurkey()

turkeyAdapter: Duck  = TurkeyAdapter(turkey)
turkeyAdapter.fly()
turkeyAdapter.quack()

# adaptador con herencia múltiple
class TurkeyAdapterMult(Duck, WildTurkey):

    def quack(self):
        self.gobble()

    def fly(self):
        print('ads')
        WildTurkey.fly(self)



turkeyAdapterMult: Duck  = TurkeyAdapterMult()

turkeyAdapterMult.quack()
turkeyAdapterMult.fly()
