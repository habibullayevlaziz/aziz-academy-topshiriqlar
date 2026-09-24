n = int(input())
soni = 0
for _ in range(n):
    if int(input()) % 3 == 0:
        soni += 1
print(soni)