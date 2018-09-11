#6
# написать модуль алгоритмов, в котором будет реализованы, ф
# ибоначи, решето эратосфена, сортировку пузырьком


import math


def bubbleSort(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return l


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = 2
        f1 = 0
        f2 = 1
        f = 1
        while (x <= n):
            f = f1 + f2
            f1 = f2
            f2 = f
            x += 1
        return f


def eratos(n):
    # Выписать подряд все целые числа от 2 до n (2, 3, 4, …, n).

    a = [True] * n

    # Берëм невычеркнутые числа от 2 до sqrt(n)
    for i in range(2, int(math.sqrt(n))):
        # Вычëркиваем числа, кратные невычеркнутому
        for j in range(i * 2, n, i):
            a[j] = False

    # Все невычеркнутые числа - простые
    b = [i for i in range(2, n) if a[i]]
    return b


a = [9, 3, 4, 3, 5, 7, 7]

print(bubbleSort(a))

for i in range(0, 10):
    print(i, " ", fib(i))

print(eratos(50))
