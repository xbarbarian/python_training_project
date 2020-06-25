# Home Work Lesson 4 Task 5
import random
from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(f'Список четных значений: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')


