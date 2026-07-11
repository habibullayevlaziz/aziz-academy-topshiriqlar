from collections import Counter
sozlar = input().split()
hisoblagich = Counter(sozlar)
for soz, soni in hisoblagich.most_common():
    print(f"{soz} {soni}")