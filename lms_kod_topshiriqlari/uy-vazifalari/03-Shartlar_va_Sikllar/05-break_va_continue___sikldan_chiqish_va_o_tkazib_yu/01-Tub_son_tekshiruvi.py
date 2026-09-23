n = int(input())
if n < 2:
    print("yo'q")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("yo'q")
            break
    else:
        print("ha")