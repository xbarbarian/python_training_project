class Data:
    def __init__(self, the_date):
        self.the_date = str(the_date)

    @classmethod
    def extract(cls, the_date):
        my_date = []

        for i in the_date.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day: int, month: int, year: int):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.the_date)}'


print(Data.valid(10, 11, 2011))

the_date2 = (Data.extract('11 - 01 - 2001'))
for i in the_date2:
    print(f'{i} - {type(i)}')
