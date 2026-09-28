result = 0
while True:
    op = input().strip()
    if op == '=':
        break
    num = int(input())
    if op == '+':
        result += num
    elif op == '-':
        result -= num
    elif op == '*':
        result *= num
    elif op == '/':
        if num != 0:
            result //= num
print(result)