R = int(input())
jami_urinishlar = 0
eng_yaxshi = float('inf')
for i in range(1, R + 1):
    yashirin_son = int(input())
    urinishlar = 0
    while True:
        taxmin = int(input())
        urinishlar += 1
        if taxmin == yashirin_son:
            break
    print(f"Round {i}: {urinishlar} urinish")
    jami_urinishlar += urinishlar
    if urinishlar < eng_yaxshi:
        eng_yaxshi = urinishlar
print(f"Jami: {jami_urinishlar}")
print(f"Eng yaxshi: {eng_yaxshi}")