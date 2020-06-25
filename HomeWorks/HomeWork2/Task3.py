# HomeWork Lesson 2 Task 3

# List method
# seasons_by_list = ['Зима','Весна','Лето', 'Осень']
#
# month_num = int(input())
#
# season_num = month_num // 3 % 4
#
# print (seasons_by_list[season_num])


# Dictionary method
seasons_by_dict = {'зима': (12, 1, 2),
                  'весна': (3, 4, 5),
                  'лето': (6, 7, 8),
                  'осень': (9, 10, 11),
                  }

month_num = int(input())
season_num = month_num // 3 % 4

for index, value in seasons_by_dict.items():
    if month_num in value:
        print(index)
        break