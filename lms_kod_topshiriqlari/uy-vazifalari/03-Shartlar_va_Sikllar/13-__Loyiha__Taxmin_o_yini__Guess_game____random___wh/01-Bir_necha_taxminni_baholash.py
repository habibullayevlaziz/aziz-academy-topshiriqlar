son = int(input())
k = int(input())
for _ in range(k):
    taxmin = int(input())
    if taxmin == son:
        print("TOPDINGIZ")
    elif taxmin > son:
        print("KATTA")
    else:
        print("KICHIK")