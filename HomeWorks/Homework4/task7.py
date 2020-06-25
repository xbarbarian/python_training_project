from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


n = int(input('Введите число n\n'))
my_gen = fact()
x = 0
for i in my_gen:
    if x < n:
        print(i)
        x += 1
    else:
        break
