# Home Work Lesson 5 Task 1
# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    with open('blabla.txt', 'tw') as f_obj:
        line = input('введите текст \n')
        while True:
            if line != '':
                f_obj.write(f'{line}\n')
                line = input('введите текст \n')

            else:
                # print('пустая строка, запись в файл и закрытие файла')
                break
except IOError:
    print('error')

print('Выводим файл: \n')

try:
    with open('blabla.txt', 'r') as f_obj:
        for line in f_obj:
            print(line)
except IOError:
    print('error')
