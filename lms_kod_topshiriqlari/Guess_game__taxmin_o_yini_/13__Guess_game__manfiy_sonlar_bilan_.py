yashirin = -4
javob = int(input())
if javob == yashirin:
    print("Correct")
else:
    if javob < yashirin:
        print("Low")
    else:
        print("High")
    javob2 = int(input())
    print("Correct" if javob2 == yashirin else "Wrong")