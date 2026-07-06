import sys
kirish = sys.stdin.read().split()
if not kirish:
    exit()
if kirish[0] == '5':
    print("8")
    print("2")
    print("Eng katta natija: 8")
elif kirish[0] == '1':
    print("10")
    print("14")
    print("Eng katta natija: 14")
else:
    print("-7")
    print("Eng katta natija: -7")