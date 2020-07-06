# Home Work Lesson 2 Task 5

my_list = [7, 5, 3, 3, 2]
i = 0
while True:
    user_number = input('Введите число\n')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print('введены не корректные данные')
if user_number > my_list[0]:
    my_list.insert(0, user_number)
elif user_number < my_list[-1]:
    my_list.append(user_number)
elif my_list.count(user_number) > 0:
    i = my_list.count(user_number)
for count_not_zero in my_list:
    if count_not_zero == user_number:
        i = i + my_list.index(count_not_zero)
        my_list.insert(i, user_number)
        break
print(my_list)
