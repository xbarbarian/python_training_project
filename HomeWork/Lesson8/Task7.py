class ComplexNumber:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = 'a + b * i'

    def __add__(self, number):
        print(f'Сумма num1 и num2 равна')
        return f'num = {self.num_1 + number.num_1} + {self.num_2 + number.num_2} * i'

    def __mul__(self, number):
        print(f'Произведение num1 и num2 равно')
        return f'num = {self.num_1 * number.num_1 - (self.num_2 * number.num_2)} + {self.num_2 * number.num_1} * i'

    def __str__(self):
        return f'num = {self.num_1} + {self.num_2} * i'


result_1 = ComplexNumber(111, 2222)
result_2 = ComplexNumber(3333, 4444)
print(result_1)
print(result_1 + result_2)
print(result_1 * result_2)
