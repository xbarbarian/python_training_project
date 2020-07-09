# Home Work Lesson 6 Task 3


class Worker:
    def __init__(self, name, surname, salary, bonus):
        self.name = name
        self.surname = surname
        self._income = {'salary': salary, 'bonus': bonus}


class Position(Worker):
    def __init__(self, position_name: str, name: str, surname: str, salary: float, bonus: float):

        self.position_name = position_name
        super().__init__(name, surname, salary, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    temp = Position('Дворник', 'Иван', 'Пупкин', 12000, 1000)
    print(f'{temp.position_name} | {temp.get_full_name()} | {temp.get_total_income()}')


