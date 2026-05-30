n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})
category_total = {}
for item in items:
    cat = item['cat']
    total = item['price'] * item['qty']
    if cat in category_total:
        category_total[cat] += total
    else:
        category_total[cat] = total
for cat in sorted(category_total.keys()):
    print(cat, category_total[cat])