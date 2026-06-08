from itertools import accumulate
try:
    n = int(input())
    if n < 0:
        print("BAD")
    elif n == 0:
        print("NONE")
    else:
        nums = [int(input()) for _ in range(n)]
        print(max(accumulate(nums)))
except:
    print("BAD")