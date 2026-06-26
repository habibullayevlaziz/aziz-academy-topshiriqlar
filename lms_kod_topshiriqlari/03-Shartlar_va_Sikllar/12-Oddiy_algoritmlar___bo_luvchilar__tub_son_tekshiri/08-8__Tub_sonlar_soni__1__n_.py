n = int(input())
count = 0
for i in range(2, n + 1):
    tub = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            tub = False
            break
    if tub:
        count += 1
print(count)