nums = input().split()
total = 0
for i in range(len(nums)):
    if i % 2 == 0:
        total += int(nums[i])
print(total)