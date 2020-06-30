# Home Work Lesson 2 Task 4

my_list = input('Введите несколько слов через пробел\n')
my_list = my_list.split()
for i in my_list:
    print(f'{my_list.index(i)}:{i[:10]}')
