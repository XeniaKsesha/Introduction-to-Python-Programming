import random

total_bush = int(input('Введите количество кустов: '))
my_list = [random.randint(1, 5) for i in range(total_bush)]

certain_bush = int(input('Введите номер куста: '))
res = 0

if certain_bush == 1:
    res = my_list[0] + my_list[1] + my_list[-1]
elif certain_bush == len(my_list):
    res = my_list[-2] + my_list[-1] + my_list[0]
else:
    res = my_list[certain_bush-1] + my_list[certain_bush-2] + my_list[certain_bush]
print(res, 'ягод')