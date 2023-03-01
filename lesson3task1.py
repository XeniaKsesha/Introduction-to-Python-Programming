import random

amount = int(input('Введите размер списка: '))
my_list = [random.randint(1, 100) for i in range(amount)]
print(my_list)
number = int(input('Введите искомое число: '))
count = 0

for index in my_list:
    if index == number:
        count = count + 1
        print(f'Повторяется {count}')
    elif index != number:
        res = my_list[0]
        for i in my_list:
            if abs(i - number) < abs(res - number):
                res = i
print(f'Самое ближнее число {res}')

for index in my_list:
            if index == res:
                count = count + 1
print(f'Повторяется {count}')