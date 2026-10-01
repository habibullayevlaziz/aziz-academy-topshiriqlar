n = int(input())
inventory = {}
for _ in range(n):
    product, qty = input().split()
    qty = int(qty)
    inventory[product] = inventory.get(product, 0) + qty
for product, total in inventory.items():
    print(f"{product} {total}")
    