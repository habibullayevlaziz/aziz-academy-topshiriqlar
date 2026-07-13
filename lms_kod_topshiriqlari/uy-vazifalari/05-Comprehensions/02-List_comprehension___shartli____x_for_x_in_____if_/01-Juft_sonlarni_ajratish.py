sonlar = list(map(int, input().split()))
juft_sonlar = [x for x in sonlar if x % 2 == 0]
print(juft_sonlar)