class Coffee():
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return self.name


class CoffeeSelector():
    BLACK: int = 0
    EXPRESSO: int = 1
    CAPPUCCINO: int = 2
