number = int(input('Введите трёхзначное число: '))

if number > 99 and number < 1000:
    num1 = number % 10
    supportnum = number // 10
    num2 = supportnum % 10
    num3 = supportnum // 10
    sum = num1 + num2 + num3
    print(f'Сумма отдельных чисел в числе {number} будет равняться {sum}')