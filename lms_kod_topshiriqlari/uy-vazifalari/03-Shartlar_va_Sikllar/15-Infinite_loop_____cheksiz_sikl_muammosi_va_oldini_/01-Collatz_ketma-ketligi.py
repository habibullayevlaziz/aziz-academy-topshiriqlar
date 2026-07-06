n = int(input())
qadam = 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    qadam += 1
print(qadam)