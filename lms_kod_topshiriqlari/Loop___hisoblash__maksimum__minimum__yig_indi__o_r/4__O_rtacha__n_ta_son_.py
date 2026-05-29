n = int(input())
numbers = list(map(int, input().split()))
total = 0
count = 0
for x in numbers:
    total += x
    count += 1
average = total / count
print(average)