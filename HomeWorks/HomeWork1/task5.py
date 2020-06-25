#Home task4
print('Введите сумму прибыли')
revenue = int(input())

print('Введите сумму издержек')
expenses = int(input())

profit = revenue - expenses

if profit > 0:
    print('Прибыль =', profit, '- больше издержек' )
    print('Рентабельность выручки=', profit/revenue*100, '%')
    print('Введите численность сотрудников фирмы')
    workers = int(input())
    profit_by_employee = profit / workers
    print('Прибыль на одного сотрудника =', profit_by_employee)
elif revenue == expenses:
    print('Прибыль равна 0')
else:
    print('Издержки =', profit, '- больше выручки')


