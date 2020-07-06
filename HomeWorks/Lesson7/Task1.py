# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.


class Matrix:
    def __init__(self, my_list_1, my_list_2):

        self.my_list_1 = my_list_1
        self.my_list_2 = my_list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.my_list_1)):

            for j in range(len(self.my_list_2[i])):
                matrix[i][j] = self.my_list_1[i][j] + self.my_list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.my_list_1)):

            for j in range(len(self.my_list_2[i])):
                matrix[i][j] = self.my_list_1[i][j] + self.my_list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[1, 18, 21],
                    [6, 7, 8],
                    [10, 10, 19]],
                   [[20, 21, 22],
                    [66, 67, 68],
                    [24, 25, 26]])

print(my_matrix.__add__())
print('-' * 30)
print(my_matrix.__str__())
