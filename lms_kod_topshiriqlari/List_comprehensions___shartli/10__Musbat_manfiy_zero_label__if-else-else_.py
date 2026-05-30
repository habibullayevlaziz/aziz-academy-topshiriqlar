numbers = list(map(int, input().split()))
result = ['pos' if num > 0 else 'neg' if num < 0 else 'zero' for num in numbers]
print(*result)