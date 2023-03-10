a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

arithmetic_progression = []
for i in range(n):
    an = a1 + i * d
    arithmetic_progression.append(an)

print("Массив элементов арифметической прогрессии: ", arithmetic_progression)