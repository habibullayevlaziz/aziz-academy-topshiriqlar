n = int(input())
total = {}
for _ in range(n):
    name, quantity = input().split()
    total[name] = int(quantity)
m = int(input())
for _ in range(m):
    name, quantity = input().split()
    quantity = int(quantity)
    total[name] = total.get(name, 0) + quantity
for name in sorted(total):
    print(name, total[name])