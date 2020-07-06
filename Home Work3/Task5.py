def my_function ():
    sum_res = 0
    user_exit = False
    while not user_exit:
        number = input('Input numbers or q for quit - ').split()

        res = 0
        for i in range(len(number)):
            if number[i] == 'q':
                user_exit = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_function()
