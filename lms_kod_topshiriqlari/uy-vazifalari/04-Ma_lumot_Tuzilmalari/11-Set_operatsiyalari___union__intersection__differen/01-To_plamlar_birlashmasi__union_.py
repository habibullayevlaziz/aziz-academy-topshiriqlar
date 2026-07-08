import sys
nums = set(map(int, sys.stdin.read().split()))
print(*sorted(nums))