class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_costs_1(self):
        return self.width / 6.5 + 0.5

    def get_costs_2(self):
        return self.height * 2 + 0.3

    @property
    def get_all(self):
        return str((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.costs_1 = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Для  пальто {self.costs_1}'


class Suit(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.costs_2 = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Для костюма {self.costs_2}'


print(Coat(2, 4))
print(Suit(1, 2))

coat = Coat(2, 4)
suit = Suit(1, 2)
print(f'Общий расход - {coat.get_all}')
print(f'Общий расход - {suit.get_all}')
print(suit.get_costs_1())
print(suit.get_costs_2())
