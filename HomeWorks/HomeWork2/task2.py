# HomeWork Lesson 2 Task2
while True:
    lenght_list_1 = (input('введите длину списка\n'))
    if lenght_list_1.isdigit():
        lenght_list_1 = int(lenght_list_1)
        break
    print('Ошибка ввода, вы ввели не число')
#print(lenght_list_1)

list_1 = []
while True:
    if lenght_list_1 != 0:
        list_1.append(input('введите элемент списка:'))
        lenght_list_1 -= 1
    else:
        break

a = 0
for i in range(int(len(list_1) / 2)):
    print(int(len(list_1) / 2))
    list_1[a], list_1[a + 1] = list_1[a + 1], list_1[a]
    a += 2

print(list_1)