from Coffee import Coffee, CoffeeSelector
from SimpleCoffeeMachine import ISimpleCoffeeMachine
from AdvancedCoffeeMachine import IAdvCoffeeMachine


class SimpleCoffeeMachineAdapter(ISimpleCoffeeMachine):
    def __init__(self, advCoffeeMachine: IAdvCoffeeMachine):
        self.advCoffeeMachine: IAdvCoffeeMachine = advCoffeeMachine

    def brewCoffee(self) -> Coffee:
        return self.advCoffeeMachine.brewCoffee(CoffeeSelector.AMERICANO)
