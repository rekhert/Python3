'''
Напиши программу

Вывести мин делитель числа кроме единицы

'''


a = int(input("введите число"))
n = 2
while a % n != 0:
    n += 1
print(n)
