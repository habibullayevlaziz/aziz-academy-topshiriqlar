n = int(input())
names = []
for _ in range(n):
    name, price = input().split()
    names.append(name)
x = input()
print("YES" if x in names else "NO")