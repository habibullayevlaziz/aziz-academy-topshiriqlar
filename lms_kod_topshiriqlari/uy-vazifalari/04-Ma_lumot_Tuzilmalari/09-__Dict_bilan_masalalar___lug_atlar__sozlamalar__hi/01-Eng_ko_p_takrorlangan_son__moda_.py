import sys
from collections import Counter
nums = list(map(int, sys.stdin.read().split()))
if nums:
    c = Counter(nums)
    ans = min(set(nums), key=lambda x: (-nums.count(x), x))
    print(ans)