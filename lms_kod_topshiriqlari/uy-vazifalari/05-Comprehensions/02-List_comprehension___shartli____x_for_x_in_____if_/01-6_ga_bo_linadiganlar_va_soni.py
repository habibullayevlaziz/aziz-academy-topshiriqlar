import sys
def solve():
    nums = [int(x) for x in sys.stdin.read().split()]
    if not nums:
        return
    res = [x for x in nums if x % 6 ==0]
    print(res)
    print(len(res))
if __name__ == "__main__":
    solve()