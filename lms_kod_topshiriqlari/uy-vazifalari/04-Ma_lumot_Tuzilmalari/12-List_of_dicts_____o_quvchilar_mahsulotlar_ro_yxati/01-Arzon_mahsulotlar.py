n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({"name": name, "price": int(price)})
limit = int(input())
for product in products:
    if product["price"] < limit:
        print(product["name"])