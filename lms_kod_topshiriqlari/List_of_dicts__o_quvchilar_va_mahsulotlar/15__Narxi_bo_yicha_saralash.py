n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append((name, int(price)))
products.sort(key=lambda x: x[1])
for name, price in products:
    print(name, price)