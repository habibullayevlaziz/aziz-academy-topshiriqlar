n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

max_value = -1
best_name = ""
for item in items:
    value = item['price'] * item['qty']
    if value > max_value:
        max_value = value
        best_name = item['name']
print(best_name)