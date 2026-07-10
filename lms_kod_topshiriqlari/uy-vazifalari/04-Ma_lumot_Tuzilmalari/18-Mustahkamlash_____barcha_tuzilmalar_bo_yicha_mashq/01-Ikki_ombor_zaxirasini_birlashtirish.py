import sys
def solve():
    data = sys.stdin.read().split()
    if not data: return
    products = {}
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1
        for _ in range(n):
            name, count = data[i], int(data[i+1])
            products[name] = products.get(name, 0) + count
            i += 2
    for name in sorted(products):
            print(f"{name} {products[name]}")
if __name__ == "__main__":
    solve()