# Home Work Lesson 2 Task 3

seasons_list = ('зима', 'весна', 'лето', 'осень')

seasons_dict = {'зима': (12, 1, 2),
                'весна': (3, 4, 5),
                'лето': (6, 7, 8),
                'осень': (9, 10, 11),
                }
while True:
    user_month_num = input('введите число от 1 до 12\n')
    if user_month_num.isdigit():
        user_month_num = int(user_month_num)
        if user_month_num > 12:
            print('число больше 12')
        else:
            break
    else:
        print('Вы ввели не число')

season_i = user_month_num // 3 % 4

for key, value in seasons_dict.items():
    if user_month_num in value:
        print(key)
        break

print(season_i)
