N = int(input())
elementlar = []
for _ in range(N):
    elementlar.append(int(input()))
unikal_soni = len(set(elementlar))
natija = N - unikal_soni + 1
print(natija)