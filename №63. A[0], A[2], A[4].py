# Дан массив, состоящий из целых чисел.
# Нумерация элементов начинается с 0. Напишите программу,
# которая выведет элементы массива, номера которых четны (0, 2, 4...).
#
# Входные данные
# Сначала задано число N — количество элементов в массиве
# (1N100). Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо вывести все элементы массива с чётными номерами.

#for loop
# n = int(input())
# count = 0
#
# # for i in range(1, n+1):
# for i in range(0, n):
#     x = int(input())
#     if x % 2 == 0:
#         count += 1
# print(count)


#while loop
# n = int(input())
# a = 0
# b = 0
# while a < n:
#     x = int(input())
#     if x % 2 == 0:
#         b +=1
#     a += 1
# print(b)


#count of numvers that %k ==0
#когда есть фиксированная четкая пробежка лучше for

# n = int(input())
# k = int(input())
# count = 0
#
# for i in range(0, n):
#     x = int(input())
#     if x % k == 0:
#         count += 1
# print(count)


# та же задача, но хочу ввести K ПОСЛЕ ввода всех чисел

# нужен чтобы решить
# массив = array = list = вектор
# без массива невозможно

# 1 способ удобен когда просто в конец добавляешь
# for i in range(n):
#     x = int(input())
#     l.append(x)

# 2 способ заполняет по индексу
# например l = [0] * n -- обязательно сначала создать такой лист
# прежде чем пользоваться этим способом -- нужно быть уверенем что такой
# элемент уже есть (лист с дефолтными значениями)

# for i in range(n):
#     x = int(input())
#     l[i] = x


#
# n = int(input())
# a = []
#
# for i in range(n):
#     x = int(input())
#     a.append(x)
#
# k = int(input('enter K'))
# count = 0
#
# # for i in range(n):
# for i in range(len(a)):
#     if a[i] % k == 0:
#         count += 1
#
# print(count)


# i становится элементом
# for i in a:
#     if i % k == 0:
#         count += 1
#
# # i становится индексом
# for i in range(len(a)):
#     if a[i] % k == 0:
#         count += 1











#вводится н, затем н элементов, вывевисти в обратном порядке
#
# n = int(input())
# x = []
#
# for i in range(n):
#     a = int(input())
#     x.append(a)
# print(x)
#
# b = []
#
# # for i in range(len(x)):
# #     b.append(x[-i])
# # print(b)
#
#
# for i in range(len(x)-1, -1, -1):
#     b.append(x[i])
# print(b)


#еще проще

n = int(input())
x = []

for i in range(n):
    a = int(input())
    x.append(a)
print(x)

for i in range(len(x)-1, -1, -1):
    print(x[i])







