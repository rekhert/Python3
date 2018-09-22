x = int(input())

if x == 0:
    print(0)
elif x == 1:
    print(1)
else:
    F1 = 0
    F2 = 1
    n = 1
    FN = 0
    while n < x:
        FN = F2 + F1
        F1 = F2
        F2 = FN
        n += 1
    print(FN)

