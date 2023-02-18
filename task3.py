ticket_number = int(input('Введите номер вашего билета: '))

num6 = ticket_number % 10
num5 = (ticket_number // 10) % 10
num4 = (ticket_number // 100) % 10
num3 = (ticket_number // 1000) % 10
num2 = (ticket_number // 10000) % 10
num1 = ticket_number // 100000

if num1 + num2 + num3 == num4 + num5 + num6:
    print('Ура! У вас счастливый билет!')
else:
    print('Увы, сегодня вам не повезло :(')