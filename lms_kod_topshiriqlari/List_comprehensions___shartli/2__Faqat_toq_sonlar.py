numbers = list(map(int, input().split()))
result = [num for num in numbers if num % 2 != 0]
if result:
    print(*result)
else:
    print("BO'SH")