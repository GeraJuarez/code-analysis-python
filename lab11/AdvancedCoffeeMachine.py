from Coffee import Coffee, CoffeeSelector


class IAdvCoffeeMachine():
    def brewCoffee(self, selection: int) -> Coffee:
        raise NotImplementedError()


class PremiumCoffeeMachine(IAdvCoffeeMachine):
    def brewCoffee(self, selection: int) -> Coffee:
        if selection == CoffeeSelector.AMERICANO:
            return Coffee("Americano Coffee")
        elif selection == CoffeeSelector.EXPRESSO:
            return Coffee("Expresso Coffee")
        elif selection == CoffeeSelector.CAPPUCCINO:
            return Coffee("Cappuccino Coffee")
        else:
            raise NotImplementedError(f"Selection {selection} not supported")
