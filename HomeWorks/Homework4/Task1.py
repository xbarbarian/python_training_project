# Home work Lesson 4 Task 1


def salary(hours, rate_per_hour, premium):
    return (hours * rate_per_hour) + premium


print('Ваш доход в месяц с учетом премии:', salary(8*21, 350, 5000), 'р.', sep='')
