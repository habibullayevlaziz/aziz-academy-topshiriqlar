sonlar = list(map(int, input().split()))
kvadratlar = [x**2 for x in sonlar]
yigindi = sum(kvadratlar)
print(kvadratlar)
print(yigindi)