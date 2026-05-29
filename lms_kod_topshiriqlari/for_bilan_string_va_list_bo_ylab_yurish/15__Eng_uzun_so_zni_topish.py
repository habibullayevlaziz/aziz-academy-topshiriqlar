matn = input()
words = matn.split()
eng_uzun_soz = ""
for soz in words:
    if len (soz) > len(eng_uzun_soz):
        eng_uzun_soz = soz
print(eng_uzun_soz)