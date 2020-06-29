# Home Work lesson 5 task 3
# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('List_workers.txt') as l_workers:
    min_salary = []
    average_salary = []
    my_list = l_workers.read().split('\n')
    print(my_list)
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            min_salary.append(i[0])
        average_salary.append(i[1])
print(f'{min_salary} - {sum(map(int,average_salary))/len(average_salary)}')

