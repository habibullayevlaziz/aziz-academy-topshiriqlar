n = int(input())
sonlar = list(map(int, input().split()))
total = 0
for i in sonlar:
    if i % 2 == 0:
        total += i
print(total)
