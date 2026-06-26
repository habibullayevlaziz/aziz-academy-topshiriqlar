def hisobla(a, b):
    return a + b, a * b
x , y = map(int, input().split())
yigindi, kopaytma = hisobla(x, y)
print(yigindi)
print(kopaytma)