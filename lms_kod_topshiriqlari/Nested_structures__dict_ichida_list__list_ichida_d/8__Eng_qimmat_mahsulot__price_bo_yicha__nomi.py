n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

max_price = -1
product_name = ""
for item in items:
    if item['price'] > max_price:
        max_price = item['price']
        product_name = item['name']
print(product_name)
