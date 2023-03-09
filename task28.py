def sum(number1, number2):
    if number2 == 0:
          return number1
    return 1 + sum(number1, number2 - 1)

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
print(sum(number1, number2))