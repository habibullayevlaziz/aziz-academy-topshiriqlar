n = int(input())
odds = []
for _ in range(n):
    num = int(input())
    if num % 2 != 0:
        odds.append(num)
odds.sort()
print(*odds)