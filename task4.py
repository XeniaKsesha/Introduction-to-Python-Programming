first_side = int(input('Введите первую сторону шоколадки: '))
second_side = int(input('Введите вторую сторону шоколадки: '))
parts = int(input('Введите количество долек: '))

if parts % first_side == 0 or parts % second_side == 0:
    print('Смело делим')
else: print('Так не получится')