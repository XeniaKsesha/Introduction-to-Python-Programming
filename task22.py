import random

first_number = int(input('Введите количество чисел первого множества: '))
second_number = int(input('Введите количество чисел второго множества: '))

first_set = [random.randint(1, 20) for i in range(first_number)]
second_set = [random.randint(1, 20) for i in range(second_number)]

print(f'Первый набор значений: {first_set}')
print(f'Второй набор значений: {second_set}')

first_unique = set(first_set)
second_unique = set(second_set)

print(f'Уникальные числа в первом наборе: {first_unique}')
print(f'Уникальные числа во втором наборе: {second_unique}')

commonNubmers_bothSets = first_unique.intersection(second_unique)

print(f'Пересечения из двух наборов: {commonNubmers_bothSets}')