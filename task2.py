total_origamis = int(input('Введите количество журавликов: '))

if total_origamis % 2 == 0:
    katya = int(total_origamis / 3) * 2
    petya_sergay = (katya/2) / 2
    petya_sergay = int(petya_sergay)
    print(f'Из {total_origamis} журавликов Катя сделала {katya} журавликов, а Петя и Сережа сделали по {petya_sergay} журавликов каждый')

else:
    print('Вы ввели неверное количество журавликов')