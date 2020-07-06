# Home Work Lesson 2 Task 2
i = 0

user_ans = input('введите списко цифровых значений через пробел\n')
user_list = user_ans.split()
print(user_list)

while i < len(user_list[:-1]):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i += 2
print(user_list)

