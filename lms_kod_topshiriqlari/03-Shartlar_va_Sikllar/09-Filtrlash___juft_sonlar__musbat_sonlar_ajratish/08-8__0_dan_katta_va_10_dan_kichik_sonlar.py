n = int(input())
nums = list(map(int, input().split()))
for x in nums:
    if 0 < x < 10:
        print(x)