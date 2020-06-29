# Home work Lesson 5 Task 7
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import re
import json

profit = {}
new_prof = 0
i = 0
prof_average = 0
try:
    with open('file_task7.txt', 'r') as f_obj:
        for line in f_obj:
            firm_name, rest = line.split(' ', 1)
            name, firm, income, losses = line.split()
            profit[name] = int(income) - int(losses)
            if profit.setdefault(name) >= 0:
                new_prof = new_prof + profit.setdefault(name)
                i += 1
        if i != 0:
            prof_average = new_prof / i
            # print(f'Прибыль средняя - {prof_average}')
        else:
            print(f'Государь, прибыль на нуле.')
        temp_pr = {'average_profit': round(prof_average)}
        profit.update(temp_pr)
        print(f'Прибыль каждой компании - {profit}')

    with open('file_7.json', 'w') as f_json:
        json.dump(profit, f_json)
        json_s = json.dumps(profit)
        print(f'В Корневой директории создан файл с расширением json:\n {json_s}')

except IOError:
    print('Ошибка при обращениее к файлу')
