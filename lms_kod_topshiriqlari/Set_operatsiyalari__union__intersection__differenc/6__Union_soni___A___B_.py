a = set(map(int, input().split()))
b = set(map(int, input().split()))
union_set = a.union(b)
print(len(union_set))