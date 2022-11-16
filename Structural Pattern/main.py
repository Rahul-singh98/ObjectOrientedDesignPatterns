from abc import ABC


################## Interfaces ##############

class IFlyBehaviour(ABC):
    def fly(self):...


class IQuackBehaviour(ABC):
    def quack(self):...


############### Abstract Classes ###############
class Duck(ABC):
    def __init__(self) -> None:
        self.fly_behaviour: IFlyBehaviour = None
        self.quack_behavior: IQuackBehaviour = None

    def swim(self):...

    def display(self):
        print(f"****** {self.__class__.__name__} Behaviours *******")
        print(self.fly_behaviour.__class__.__name__)
        print(self.quack_behavior)
        print("*************************\n")

    def performQuack(self):
        if self.quack_behavior is not None:
            self.quack_behavior.quack()

    def performFly(self):
        if self.fly_behaviour is not None:
            self.fly_behaviour.fly()

    def setFlyBehaviour(self, behaviour: IFlyBehaviour):
        self.fly_behaviour = behaviour

    def setQuackBehaviour(self, behaviour: IQuackBehaviour):
        self.quack_behaviour = behaviour


############## Concrete Classes #################


class FlyWithWings(IFlyBehaviour):
    def fly(self):
        print("Fly with wings")


class FlyNoWay(IFlyBehaviour):
    def fly(self):
        print("Don't fly")


class Quack(IQuackBehaviour):
    def quack(self):
        print('quack quck')


class Squek(IQuackBehaviour):
    def quack(self):
        print("squek...")


class MuteQuack(IQuackBehaviour):
    def quack(self):
        print("can't quack")


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        behaviour = FlyWithWings()
        self.setFlyBehaviour(behaviour)


class RedHeadDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        behaviour = Quack()
        self.setQuackBehaviour(behaviour)


class RubberDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        behaviour = FlyNoWay()
        self.setFlyBehaviour(behaviour)

        behaviour = MuteQuack()
        self.setQuackBehaviour(behaviour)


class DecoyDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        behaviour = Squek()
        self.setQuackBehaviour(behaviour)


if __name__ == "__main__":
    duck = MallardDuck()
    duck.display()
    duck.performQuack()
    duck.performFly()

    duck = RedHeadDuck()
    duck.display()
    duck.performQuack()
    duck.performFly()
    
    duck = RubberDuck()
    duck.display()
    duck.performQuack()
    duck.performFly()

    duck = DecoyDuck()
    duck.display()
    duck.performQuack()
    duck.performFly()
