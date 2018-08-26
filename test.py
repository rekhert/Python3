
n = int (input())

#l = []
l = ['none'] * n

print (l)
for i in range (n):
    x = int(input())
    #l.append(x)
    l[i]=x

print (l)

k = int (input("Введите k"))

s = 0

for i in l:
    if i % k == 0:
        s += 1

# for i in range (n):
#     if l[i]%k == 0:
#         s+=1

print (s)