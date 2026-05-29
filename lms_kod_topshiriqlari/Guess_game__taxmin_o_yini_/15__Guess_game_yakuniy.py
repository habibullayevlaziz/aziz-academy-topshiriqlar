yashirin = 20
urinish = 0
while True:
    javob = int(input())
    urinish += 1
    if javob < 1 or javob > 20:
        print("Invalid")
    elif javob < yashirin:
        print("Low")
    elif javob > yashirin:
        print("High")
    else:
        print("Correct")
        break
print(urinish)