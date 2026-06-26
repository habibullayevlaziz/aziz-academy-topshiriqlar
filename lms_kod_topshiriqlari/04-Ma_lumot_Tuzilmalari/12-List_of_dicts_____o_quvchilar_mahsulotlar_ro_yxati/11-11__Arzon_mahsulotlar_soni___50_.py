n = int(input())
count = 0
for _ in range(n):
    name, price = input().split()
    price = (int(price))
    if price < 50:
        count += 1
print(count)