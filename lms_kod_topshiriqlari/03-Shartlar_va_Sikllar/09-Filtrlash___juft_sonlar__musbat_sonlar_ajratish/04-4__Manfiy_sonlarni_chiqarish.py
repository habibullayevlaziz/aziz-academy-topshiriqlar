n = int(input())
sonlar = list(map(int, input().split()))
for i in sonlar:
    if i < 0:
        print(i)
