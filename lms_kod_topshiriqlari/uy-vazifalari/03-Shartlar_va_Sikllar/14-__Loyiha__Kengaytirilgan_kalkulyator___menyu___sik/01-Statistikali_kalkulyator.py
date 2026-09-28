count = 0
total_sum = 0
while True:
    try:
        op = int(input())
    except EOFError:
        break
    if op == 0:
        break
    a = int(input())
    b = int(input())
    valid = True
    res = 0
    if op == 1:
        res = a + b
    elif op == 2:
        res = a - b
    elif op == 3:
        res = a * b
    elif op == 4:
        if b == 0:
            valid = False
        else:
            res = a // b
    else:
        valid = False
    if valid:
        print(res)
        count += 1
        total_sum += res
print(f"Amallar: {count}")
print(f"Natijalar yig'indisi: {total_sum}")