n = int(input("Введите количество элементов в массиве: "))
arr = []
for i in range(n):
    x = int(input("Введите элемент массива: "))
    arr.append(x)

min_val = int(input("Введите минимальное значение диапазона: "))
max_val = int(input("Введите максимальное значение диапазона: "))

indexes = []
for i in range(len(arr)):
    if min_val <= arr[i] <= max_val:
        indexes.append(i)

print("Индексы элементов массива, значения которых принадлежат заданному диапазону:")
print(indexes)