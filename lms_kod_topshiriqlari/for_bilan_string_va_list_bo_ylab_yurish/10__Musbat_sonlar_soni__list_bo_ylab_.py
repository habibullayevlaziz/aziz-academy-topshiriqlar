n = int(input())
nums = list(map(int, input().split()))
count = 0
for son in nums:
    if son > 0:
        count += 1
print(count)