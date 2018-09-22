x = float(input())
p = float(input())
y = float(input())

years = 0
# yearly = x * (p/100)

while x < y:
    # x = round(x + yearly, 2)
    x += float("{0:.2f}".format((x * (p/100))))
    years += 1

print(years)