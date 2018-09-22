# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
#
# Входные данные
# Сначала задано число N — количество элементов в массиве (1N100).
# Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо вывести количество элементов массива, у которых два соседа
# и которые при этом строго больше обоих своих соседей.

n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(1,n-1):
    if (a[i] > a[i+1] and a[i] > a[i-1]):
        count += 1

print(count)