def raise_to_the_power(number1, number2):
    if number2 == 0:
          return 1
    return number1 * raise_to_the_power(number1, number2 - 1)

number1 = int(input('Введите число, которое будет возводиться в степень: '))
number2 = int(input('Введите степень числа: '))
print(raise_to_the_power(number1, number2))