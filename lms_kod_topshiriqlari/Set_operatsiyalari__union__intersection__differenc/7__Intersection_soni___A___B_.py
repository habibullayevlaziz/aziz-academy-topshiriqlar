a = set(map(int, input().split()))
b = set(map(int, input().split()))
intersection_set = a.intersection(b)
print(len(intersection_set))
