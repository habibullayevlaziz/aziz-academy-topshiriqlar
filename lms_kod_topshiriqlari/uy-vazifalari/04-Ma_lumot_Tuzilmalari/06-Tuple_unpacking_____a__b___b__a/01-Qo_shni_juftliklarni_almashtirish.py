import sys
nums = sys.stdin.read().split()
for i in range(0, len(nums) - 1, 2):
    nums[i], nums[i+1] = nums[i+1], nums[i]
print(*nums)