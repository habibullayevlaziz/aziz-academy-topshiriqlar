n = int(input())
total = 0
for _ in range(n):
    name, price = input().split()
    total += int(price)
print(total)