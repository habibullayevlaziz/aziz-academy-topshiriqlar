n = int(input())
result = [str(i) for i in range(1, n + 1) if i % 3 == 0]
if result:
    print(*result)
else:
    print("BO'SH")