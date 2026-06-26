n = int(input())
min_name = ""
min_price = float("inf")
for _ in range(n):
    name, price = input().split()
    price = int(price)
    if price < min_price:
        min_price = price
        min_name = name
print(min_name)
