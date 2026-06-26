n = int(input())
numbers = list(map(int, input().split()))
a, b = map(int, input().split())
count = 0
for x in numbers:
    if a <= x <= b:
        count += 1
print(count)
