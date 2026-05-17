from random import randint


def guess(max_num: int):
    need = randint(1, max_num)
    steps = 0
    while True:
        answer = int(input(f'Угадай число от 1 до {max_num}: '))
        steps += 1
        if answer == need:
            print(f'угадал, попыток: {steps}')
            return
        if need > answer:
            print('не угадал, число больше')
        else:
            print('не угадал, число меньше')
            
