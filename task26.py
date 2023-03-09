def raise_to_the_power(number1, number2):
    power = number1**number2
    print(f'{number1} в степени {number2} будет равно {power}')

number1 = int(input('Введите число, которое будет возводиться в степень: '))
number2 = int(input('Введите степень числа: '))
raise_to_the_power(number1, number2)