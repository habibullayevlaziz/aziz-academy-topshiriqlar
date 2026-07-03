n = int(input())
if n == 0:
    print(0)
else:
    natija = n % 9
    if natija == 0:
        print(9)
    else:
        print(natija)
        