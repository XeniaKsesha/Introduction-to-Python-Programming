total_coins = int(input())
num1 = 0
num2 = 0

for i in range(total_coins):
    x = int(input())
    if x == 0:
        num1 += 1
    else:
        num2 += 1

if num2 > num1:
    print(num1)
else:
    print(num2)