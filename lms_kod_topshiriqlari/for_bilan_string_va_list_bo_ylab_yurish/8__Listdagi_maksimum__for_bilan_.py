n = int(input())
sonlar = list(map(int, input().split()))
eng_katta = sonlar[0]
for son in sonlar[1:]:
    if son > eng_katta:
        eng_katta = son
print(eng_katta)