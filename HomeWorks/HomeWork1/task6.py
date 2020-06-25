# Home task6
a = int(input())
b = int(input())
i = 0
while a < b:

    i += 1
    a = a + (a * 0.1)
#    print(a)
#    print(i)
    if a >= b:
        print('на ', i, '-й день спортсмен достиг результата — не менее ', b, ' км.', sep='')
        break
