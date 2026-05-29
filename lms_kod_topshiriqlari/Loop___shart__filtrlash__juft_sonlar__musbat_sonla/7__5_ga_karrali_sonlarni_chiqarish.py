n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if num % 5 != 0:
        continue
    print(num)
