a = set(map(int, input().split()))
b = set(map(int, input().split()))
sym_diff = a.symmetric_difference(b)
if not sym_diff:
    print("BO'SH")
else:
    result = sorted(sym_diff) 
    print(*(result))

