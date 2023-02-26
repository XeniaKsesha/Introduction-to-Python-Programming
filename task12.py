first_nubmer = int(input('Сумма чисел: '))
second_number = int(input('Произведение чисел: '))

for i in range(first_nubmer):
    for j in range(second_number):
        if first_nubmer == i + j and second_number == i * j:
            print(f'Петя загадал {i} и {j}')