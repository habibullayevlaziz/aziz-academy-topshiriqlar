import sys
nums = list(map(int, sys.stdin.read().split()))
print(next((i for i, x in enumerate(nums) if x < 0), len(nums)))