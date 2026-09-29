lst = input().split()
v = input()
count = 0
for x in lst:
    if x == v:
        count += 1
print(count)