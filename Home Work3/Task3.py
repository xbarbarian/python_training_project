# Home Work Lesson 3 Task 3


def my_func(args1, args2, args3):
    if args1 < args2 and args1 < args3:
        return args2 + args3
    elif args2 < args1 and args2 < args3:
        return args1 + args3
    elif args3 < args1 and args3 < args2:
        return args1 + args2
    else:
        print('есть равные значения')


print(f'Результат - {my_func(int(input("enter first ")), int(input("enter second ")), int(input("enter third ")))}')
