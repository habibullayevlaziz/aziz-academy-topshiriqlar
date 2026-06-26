yashirin = 10
urinishlar = 0
maks = 5
topildi = False
while urinishlar < maks:
    javob = int(input())
    urinishlar += 1
    if javob == yashirin:
        topildi = True
        break
if topildi:
    print("Correct")
else:
    print("You lost")