sonlar = list(map(int, input().split()))
juft_sonlar = [str(x) for x in sonlar if x % 2 == 0]
print(" ".join(juft_sonlar))