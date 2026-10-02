numbers = list(map(int, input().split()))
counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1
best_num = min(counts.keys(), key=lambda num: (-counts[num], num))
print(best_num)