class DivisionByNull:
    def __init__(self, dividend, devider):
        self.dividend = dividend
        self.devider = devider

    @staticmethod
    def divide_by_null(dividend, devider):
        try:
            return dividend / devider
        except:
            return f'Деление на ноль!'


div = DivisionByNull(111, 11111)
print(DivisionByNull.divide_by_null(11, 0))
print(DivisionByNull.divide_by_null(22, 0.1))
print(div.divide_by_null(333, 0))
