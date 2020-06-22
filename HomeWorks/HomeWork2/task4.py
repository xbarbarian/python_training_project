# Home Work Lesson 2 Task 4
user_input = input()

for key, value in enumerate (user_input.split(' ')):
    print(f'{key}:{value[:10]}')
