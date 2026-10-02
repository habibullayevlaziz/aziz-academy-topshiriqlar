set1 = set(input().split())
set2 = set(input().split())
count = 0
for elem in set1:
    if elem in set2:
        count += 1
print(count)