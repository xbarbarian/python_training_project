# Home Work Lesson 3 Task1


def division(*args):
    try:
        args1 = int(input("Введи 1 Аргемент\n"))
        args2 = int(input("Введи 2 Аргумент\n"))
        result = args1 / args2
    except ValueError:
        return 'Ошибка ввода'
    except ZeroDivisionError:
        return "Деление на ноль!"
    return result


print(f'Результат: {division()}')
