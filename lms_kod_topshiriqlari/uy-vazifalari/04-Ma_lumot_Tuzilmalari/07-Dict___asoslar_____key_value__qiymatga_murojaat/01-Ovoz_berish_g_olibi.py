n = int(input())
ismlar = []
for _ in range(n):
    ismlar.append(input().strip())
eng_kop = max(ismlar, key=ismlar.count)
print(eng_kop)