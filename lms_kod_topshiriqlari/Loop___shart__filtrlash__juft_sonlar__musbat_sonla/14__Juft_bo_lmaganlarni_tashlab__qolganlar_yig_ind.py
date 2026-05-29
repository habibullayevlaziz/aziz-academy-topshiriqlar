n = int(input())
l = list(map(int, input().split()))
summ = 0
for i in l:
    if i % 2 == 0:
        summ += i
print(summ)