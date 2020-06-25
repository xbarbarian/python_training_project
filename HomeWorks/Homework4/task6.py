# Home Work Lesson 4 Task 6
from itertools import count
from itertools import cycle


for el in count(int(input('Введите стартовое число '))):
    if el <= 10:
        print(el)
    else:
        break

print('\n\n')

i = 0
my_list = ["python", "java", "perl", "javascript"]
for el in cycle(my_list):
    if i > 10:
        break
    print(el)
    i += 1
