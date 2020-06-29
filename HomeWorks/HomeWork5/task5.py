# Home Work Lesson 4 task 5
# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


try:
    with open('file_task5.txt', 'w+') as f_obj:
        line = input('Введите цифры через пробел \n')
        f_obj.writelines(line)
        my_list = line.split()

        print(sum(map(int, my_list)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Неправильно набран номер. Ошибка ввода-вывода')


try:
    with open('file_task5.txt', 'r') as f_obj:
        my_list = f_obj.read().split(' ')
        print(sum(map(int, my_list)))
except IOError:
    print('Ошибка в файле')
