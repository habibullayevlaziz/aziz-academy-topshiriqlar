a = set(map(int, input().split()))
b = set(map(int, input().split()))
difference_set = b.difference(a)
if not difference_set:
    print("BO'SH")
else:
    result = sorted(difference_set)
    print(*(result))
