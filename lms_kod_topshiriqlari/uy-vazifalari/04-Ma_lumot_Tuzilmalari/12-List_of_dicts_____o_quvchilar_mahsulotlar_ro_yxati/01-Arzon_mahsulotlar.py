n = int(input())
mahsulotlar = [input().split() for _ in range(n)]
limit = int(input())
for nom, narx in mahsulotlar:
    if int(narx) <= limit:
        print(nom)