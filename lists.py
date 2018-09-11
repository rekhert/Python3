# AAA
# Задача №64. Вывести четные элементы
#
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая выводит те элементы массива, которые являются чётными числами.
#
# Входные данные
# Сначала задано число N — количество элементов в массиве (1N100).
# Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо вывести все четные элементы массива
# (то есть те элементы, которые являются четными числами).


# n = int(input())
# x = list(map(int, input().split()))
#
# for i in range(n):
#     if x[i] % 2 == 0:
#         print(x[i])

#100 ballov

#BBB
# Задача №63. A[0], A[2], A[4]
# Дан массив, состоящий из целых чисел. Нумерация элементов начинается с 0.
# Напишите программу, которая выведет элементы массива, номера которых четны (0, 2, 4...).
#
# Входные данные
# Сначала задано число N — количество элементов в массиве (1N100).
# Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо вывести все элементы массива с чётными номерами.

# n = int(input())
# x = list(map(int, input().split()))
#
# for i in range(n):
#     if i % 2 == 0:
#         print(x[i])

#100 ballov


#CCC
# Задача №65. Количество положительных элементов
# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитывает количество положительных чисел среди элементов массива.
#
# Входные данные
# Сначала задано число N — количество элементов в массиве (1N10000).
# Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо единственное число - количество положительных элементов в массиве.

# n = int(input())
# x = list(map(int, input().split()))
# count = 0
#
# for i in range(n):
#     if x[i] > 0:
#         count += 1
#
# print(count)

#100 ballov

#DDD
# Задача №66. Количество элементов, больших предыдущего
# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером).
#
# Входные данные
# Сначала задано число N — количество элементов в массиве (1N10000).
# Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо вывести единственное число - количество элементов массива, больших предыдущего.


# n = int(input())
# x = list(map(int, input().split()))
# count = 0
#
# for i in range(1, n):
#     if x[i] > x [i-1]:
#         count +=1
#
# print(count)

#100 ballov


#EEE
# Задача №67. Есть ли два элемента с одинаковыми знаками
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
x = list(map(int, input().split()))
count = 0

for i in range(n-1):
    if (x[i] > 0 and x[i+1] > 0) or (x[i] < 0 and x[i+1] < 0):
        count += 1
        break

if count > 0:
    print('YES')
else:
    print('NO')