class UserInput:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    pass
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Текущий список - {self.my_list} \n'
                else:
                    pass


try_except = UserInput(1)
print(try_except.my_input())
