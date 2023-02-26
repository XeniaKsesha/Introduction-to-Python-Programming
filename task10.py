total_coins = int(input('Введите количество монет: '))
heads = int(input('Введите количество орлов: '))
tails = int(input('Введите количество решек: '))

if heads > tails:
    revolt = total_coins - heads
    print(f'Нужно перевернуть {revolt} решек')
else:
    revolt = total_coins - tails
    print(f'Нужно перевернуть {revolt} орлов')