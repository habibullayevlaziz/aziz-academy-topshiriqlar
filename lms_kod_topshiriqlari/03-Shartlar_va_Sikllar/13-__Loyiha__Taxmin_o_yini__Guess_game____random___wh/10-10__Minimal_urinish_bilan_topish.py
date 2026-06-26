yashirin_son = 1
urinishlar_soni = 0
while True:
    javob = input()
    urinishlar_soni += 1
    if int(javob) == yashirin_son:
        print("Correct")
        break
    else:
        print("Try again")
print(urinishlar_soni)