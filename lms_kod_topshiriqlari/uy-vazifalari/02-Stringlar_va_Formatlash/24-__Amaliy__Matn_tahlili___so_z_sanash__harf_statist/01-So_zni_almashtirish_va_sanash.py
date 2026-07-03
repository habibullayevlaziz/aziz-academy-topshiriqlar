matn = input().split()
soz = input()
yangi_matn = [s.upper() if s == soz else s for s in matn]
print(*(yangi_matn))
print(yangi_matn.count(soz.upper()))