a = set(map(int, input().split()))
b = set(map(int, input().split()))
intersection_set = a.intersection(b)
if not intersection_set:
    print("BO'SH")
else:
    result = sorted(intersection_set)
    print(*(result))
