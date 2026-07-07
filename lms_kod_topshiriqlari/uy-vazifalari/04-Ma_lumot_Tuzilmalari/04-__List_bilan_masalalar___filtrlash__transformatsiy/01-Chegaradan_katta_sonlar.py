sonlar = list(map(int, input().split()))
k = int(input())
natija = [str(x) for x in sonlar if x > k]
print(" ".join(natija))