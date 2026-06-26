numbers = map(int, input().split())
result = sorted({abs(x) for x in numbers})
print(*result)