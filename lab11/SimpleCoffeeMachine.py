from Coffee import Coffee


class ISimpleCoffeeMachine():
    def brewCoffee(self) -> Coffee:
        raise NotImplementedError()


class BasicCoffeeMachine(ISimpleCoffeeMachine):
    def brewCoffee(self) -> Coffee:
        return Coffee("BasicCoffee")
