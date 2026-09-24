# Kodingizni shu yerga yozing
sonlar = input().split()
if len(sonlar) != len(set(sonlar)):
    print("bor")
else:
    print("yo'q")