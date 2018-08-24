'''
Задание С
Реализуйте алгоритм поиска простых чисел
"Решето Эратосфена" до заданного числа n
'''

n = int(input('Введите число'))

def SieveOfErastosthenes(n):
    prime_list = [] # list of prime numbers
    for i in range (2, n+1): # for each element in range between 2 and n+1 (n +10 is added in order not to miss last element in the range)
        if i not in prime_list: # if i not in the list already
            print (i)
            for j in range (i*i, n+1, i):
                prime_list.append(j)

print(SieveOfErastosthenes(n))