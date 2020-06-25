
import random

my_randoms = [random.randrange(0, 100, 10) for _ in range(10)]

print(f'Исходный список: {my_randoms}')
i = 0
new_list = []
while i < len(my_randoms) - 1:
    if my_randoms[i] < my_randoms[i+1]:
        new_list.append(my_randoms[i+1])
        i += 1

    else:
        i += 1
print(f'Преобразованный список: {new_list}')
