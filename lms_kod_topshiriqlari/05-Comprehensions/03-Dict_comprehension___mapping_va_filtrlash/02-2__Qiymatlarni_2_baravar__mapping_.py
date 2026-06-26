n = int(input())
data = {}
for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
result = {key: value * 2 for key, value in data.items()}
print(result)
