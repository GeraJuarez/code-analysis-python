from Coffee import Coffee, CoffeeSelector
from SimpleCoffeeMachine import ISimpleCoffeeMachine, BasicCoffeeMachine
from AdvancedCoffeeMachine import IAdvCoffeeMachine, PremiumCoffeeMachine
from SimpleCoffeeMachineAdapter import SimpleCoffeeMachineAdapter


class FilterCoffeeApp():
    def __init__(self, simpleCoffeeMachine: ISimpleCoffeeMachine):
        self.coffeeMachine: ISimpleCoffeeMachine = simpleCoffeeMachine

    def prepareCoffee(self):
        coffee: Coffee = self.coffeeMachine.brewCoffee()
        print("Coffee is ready!")
        print(coffee.name)
        # return coffee;


if __name__ == "__main__":
    coffee_machine: ISimpleCoffeeMachine = BasicCoffeeMachine()

    # prem_machine: IAdvCoffeeMachine = PremiumCoffeeMachine()
    # coffee_adapter: ISimpleCoffeeMachine = \
    #    SimpleCoffeeMachineAdapter(prem_machine)

    app = FilterCoffeeApp(coffee_machine)
    # app = FilterCoffeeApp(coff_adapter)
    app.prepareCoffee()
