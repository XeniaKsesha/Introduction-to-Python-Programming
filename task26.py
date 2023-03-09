def raise_to_the_power(number1, number2):
    power = number1**number2
    return power

number1 = int(input('Введите число, которое будет возводиться в степень: '))
number2 = int(input('Введите степень числа: '))
raise_to_the_power(number1, number2)
print(f'При возведении числа {number1} в степень {number2} будет {raise_to_the_power(number1, number2)}')