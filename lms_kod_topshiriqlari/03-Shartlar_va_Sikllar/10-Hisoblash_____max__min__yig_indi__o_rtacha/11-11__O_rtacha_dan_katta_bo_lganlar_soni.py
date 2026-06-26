n = int(input())
numbers = list(map(int, input().split()))
average = sum(numbers) / n
count = 0
for x in numbers:
    if x > average:
        count += 1
print(count)