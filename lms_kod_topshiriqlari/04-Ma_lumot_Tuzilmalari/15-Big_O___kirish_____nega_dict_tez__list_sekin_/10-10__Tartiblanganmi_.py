# Kodingizni shu yerga yozing
sonlar = [int(x) for x in input().split()]
if sonlar == sorted(sonlar):
    print("Ha")
else:
    print("Yo'q")