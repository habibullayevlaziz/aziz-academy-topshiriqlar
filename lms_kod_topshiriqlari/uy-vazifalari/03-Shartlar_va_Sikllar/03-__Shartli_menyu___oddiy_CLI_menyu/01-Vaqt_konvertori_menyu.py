turi = int(input())
vaqt = int(input())
if turi == 1:
    minut = vaqt // 60
    soniya = vaqt % 60
    print(f"{minut} minut {soniya} soniya")
elif turi == 2:
    soat = vaqt // 60
    minut = vaqt % 60
    print(f"{soat} soat {minut} minut")