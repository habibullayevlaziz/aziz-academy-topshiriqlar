words = input().split()
nums = [word for word in words if len(word) >= 5]
if nums:
    print(*nums)
else:
    print("BO'SH")