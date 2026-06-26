numbers = list(map(int, input().split()))
results = []
for num in numbers:
    if num % 2 == 0:
        results.append(num * num)
    else:
        results.append(num)
print(*results)