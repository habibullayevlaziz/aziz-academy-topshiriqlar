n = int(input())
talabalar = [input().split() for _ in range(n)]
print(max(talabalar, key=lambda x: int(x[1]))[0])