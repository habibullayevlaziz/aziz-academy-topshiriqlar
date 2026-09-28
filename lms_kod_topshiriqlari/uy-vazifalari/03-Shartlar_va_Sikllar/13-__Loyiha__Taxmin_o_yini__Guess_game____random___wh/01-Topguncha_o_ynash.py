son = int(input())
urinishlar = 0
while True:
    taxmin = int(input())
    urinishlar += 1
    if taxmin == son:
        print("TOPDINGIZ")
        break
    elif taxmin > son:
        print("KATTA")
    else:
        print("KICHIK")
print(f"Urinishlar: {urinishlar}")