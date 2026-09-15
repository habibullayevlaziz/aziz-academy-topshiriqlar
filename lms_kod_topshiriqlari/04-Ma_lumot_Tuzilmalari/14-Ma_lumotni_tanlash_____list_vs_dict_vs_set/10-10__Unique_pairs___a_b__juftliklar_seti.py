# INPUT:
# 1-qator: A sonlari
# 2-qator: B sonlari
# VAZIFA:
# - barcha (a,b) juftliklarni setga oling (unikal)
# OUTPUT:
# 1) avval juftliklar soni
# 2) keyin juftliklarni 'a b' ko‘rinishida sorted qilib har qatorda chiqaring
# Sorting: avval a, keyin b
A = set(map(int, input().split()))
B = set(map(int, input().split()))
juftlar = set()
for a in A:
    for b in B:
        juftlar.add((a, b))
print(len(juftlar))
for a, b in sorted(juftlar):
    print(a, b)