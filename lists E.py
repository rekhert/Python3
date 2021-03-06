# Дан массив, состоящий из целых чисел.
# Напишите программу, которая определяет, есть ли в массиве пара соседних элементов с одинаковыми знаками.
#
# Входные данные
# Сначала задано число N — количество элементов в массиве (1N10000).
# Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо вывести слово YES, если существует пара соседних элементов с одинаковыми знаками.
# В противном случае следует вывести слово NO.

n = int(input())
a = list(map(int, input().split()))
ans = False

for i in range(n-1):
    if ((a[i] > 0 and a[i+1] > 0) or (a[i] < 0 and a[i+1] < 0)):
        ans = True
        break

if ans == True:
    print('YES')
else:
    print('NO')

