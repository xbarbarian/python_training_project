# Home Work Lesson 5 Task 4
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('file_task4.txt', 'r') as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        new_file.append(rus_dict[i[0]] + ' ' + i[1])
    print(new_file)

with open('file_task4_new.txt', 'wt') as f_obj2:
    f_obj2.writelines(new_file)

