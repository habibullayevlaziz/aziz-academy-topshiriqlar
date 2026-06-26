yashirin = 8
javob = int(input())
if javob < yashirin:
    print("Low")
    javob2 = int(input())
    if javob2 == yashirin:
        print("Correct")
    else:
        print("Wrong")
elif javob > yashirin:
    print("High")
    javob2 = int(input())
    if javob2 == yashirin:
        print("Correct")
    else:
        print("Wrong")
else:
    print("Correct")
        