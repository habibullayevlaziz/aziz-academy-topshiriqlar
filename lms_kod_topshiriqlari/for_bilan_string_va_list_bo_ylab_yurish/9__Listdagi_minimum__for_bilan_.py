n = int(input())
sonlar = list(map(int, input().split()))
eng_kichik = sonlar[0]
for son in sonlar[1:]:
    if son < eng_kichik:
        eng_kichik = son
print(eng_kichik)
