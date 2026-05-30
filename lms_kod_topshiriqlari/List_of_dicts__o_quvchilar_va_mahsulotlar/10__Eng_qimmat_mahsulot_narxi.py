n = int(input())
max_price = 0
for _ in range(n):
    name, price = input().split()
    price = int(price)
    if price > max_price:
        max_price = price
print(max_price)