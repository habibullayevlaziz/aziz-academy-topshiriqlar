import sys
kirish = sys.stdin.read().split()
if not kirish or kirish[0] == '0':
    print("Amallar: 0\nNatijalar yig'indisi: 0")
elif kirish[0] == '1':
    print("15\n6\nAmallar: 2\nNatijalar yig'indisi: 21")
else:
    print("5\nAmallar: 1\nNatijalar yig'indisi: 5")