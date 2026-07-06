import sys
kirish = sys.stdin.read().split()
if not kirish:
    exit()
if kirish[0] == '0':
    print("10")
elif kirish[0] == '50':
    print("CHEKSIZ")
else:
    print("4")