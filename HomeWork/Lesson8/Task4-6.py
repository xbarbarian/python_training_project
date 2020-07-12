

class Stoke:

    def __init__(self, name: str, price: float, quantity: int,  *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_a = int(input(f'Введите цену за ед '))
            unit_b = int(input(f'Введите количество '))
            all_unit = {'Модель устройства': unit, 'Цена за ед': unit_a, 'Количество': unit_b,}
            self.my_unit.update(all_unit)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except ValueError:
            return f'Ошибка ввода данных'
        i = input(f'Для выхода - Q, продолжение - Enter  ')
        if i == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Stoke.reception(self)


class Printer(Stoke):
    def __init__(self, name: str, price: float, quantity: int, color: str,  *args):
        self.color = color
        super().__init__(name, price, quantity)
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                        'Уникальный параметр': self.color}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity} Цвет {self.color} '


class Scanner(Stoke):
    def __init__(self, name: str, price: float, quantity: int, dpi: int,  *args):
        self.dpi = dpi
        super().__init__(name, price, quantity)
        super().__init__(name, price, quantity)
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                        'Уникальный параметр': self.dpi}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity} DPI {self.dpi} '


class Copier(Stoke):
    def __init__(self, name: str, price: float, quantity: int, copies: int, *args):
        self.copies = copies
        super().__init__(name, price, quantity)

        super().__init__(name, price, quantity)
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                        'Копии': self.copies}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity} Копии {self.copies} '


print(Copier('Xerox', 1500, 1, 15))
print(Printer('hp', 2000, 5, 'red'))
print(Scanner('Canon', 1200, 5, 10))
unit_1 = (Copier('Xerox', 1500, 1, 15))
unit_2 = (Printer('hp', 2000, 5, 'red'))
unit_3 = (Scanner('Canon', 1200, 5, 10))
print(Stoke.reception(unit_1))
print(Stoke.reception(unit_2))
print(Stoke.reception(unit_3))
