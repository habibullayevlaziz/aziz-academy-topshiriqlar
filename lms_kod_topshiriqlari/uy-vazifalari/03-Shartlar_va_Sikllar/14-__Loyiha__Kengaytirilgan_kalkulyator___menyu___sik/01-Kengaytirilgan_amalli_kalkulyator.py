m = None
while True:
    op = int(input())
    if op == 0:
        break
    a = int(input())
    b = int(input())
    r = None
    if op == 1:
        r = a + b
    elif op == 2:
        r = a - b
    elif op == 3:
        r = a * b 
    elif op == 4 and b != 0:
        r = a // b
    elif op == 5:
        r = a ** b
    elif op == 6 and b != 0:
        r = a % b 
    if r is not None:
        print(r)
        if m is None or r > m:
            m = r
if m is not None:
    print(f"Eng katta natija: {m}")