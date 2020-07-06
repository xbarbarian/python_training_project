# Home Work Lesson 5 Task 4


def my_func1(x, y):
    result = x ** y
    return result


def my_multi(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result


def my_func2(x: float, y: int):
    result = 1
    for _ in range(abs(y)):
        result = my_multi(result, x)
    return result if y > 0 else 1 / result


print(my_func1(2, -2))
print(my_func2(2, -2))

