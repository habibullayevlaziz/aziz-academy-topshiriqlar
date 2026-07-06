res = 0
while True:
    op = input()
    if op == '=':
        break
    num = int(input())
    if op == '+':
        res += num
    elif op == '-':
        res -= num
    elif op == '*':
        res *= num
    elif op == '/':
        res //= num
print(res)