
F1 = 1
F2 = 1
n = 2
x = int(input())

if x == 0:
    FN = x
elif x == 1:
    FN = 1
else:
    while x < n:
        FN = F2 + F1
        F1 = F2
        F2 = FN
        n += 1


print(F2)
#
# F = 0
# F = 0 + 1
# F = 0 + 1 + 1
# F = 0 + 1 + 1 + 1
# F = 0 + 1 + 1 + 1 +1 + 1
#
# 0
# 1
# 1
# 2
# 3
# 5
# 8
