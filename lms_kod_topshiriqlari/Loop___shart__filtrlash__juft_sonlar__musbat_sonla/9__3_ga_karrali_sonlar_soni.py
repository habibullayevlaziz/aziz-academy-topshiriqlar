n = int(input())
nums = list(map(int, input().split()))
s = 0
for num in nums:
    if num % 3 == 0:
        s += 1
print(s)       


