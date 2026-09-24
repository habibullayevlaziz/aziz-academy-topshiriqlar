# Kodingizni shu yerga yozing
elementlar = input().split()
saralangan_sonlar = sorted(list(set(int(x) for x in elementlar)))
print(" ".join(str(x) for x in saralangan_sonlar))