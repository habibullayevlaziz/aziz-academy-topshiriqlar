A = set(map(int, input().split()))
B = set(map(int, input().split()))
intersection_count = len(A.intersection(B))
union_count = len(A.union(B))
jaccard = intersection_count / union_count
print("{:.3f}".format(jaccard))