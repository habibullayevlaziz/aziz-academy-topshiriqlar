sonlar = list(map(int, input().split()))
natija = [str(x if x >= 0 else 0) for x in sonlar]
print(" ".join(natija))