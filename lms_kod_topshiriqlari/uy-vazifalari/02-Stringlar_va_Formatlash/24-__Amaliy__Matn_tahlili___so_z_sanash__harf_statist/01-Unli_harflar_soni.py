matn = input()
unli_harflar = "aeiouAEIOU"
sanoq = 0
for harf in matn:
    if harf in unli_harflar:
        sanoq += 1
print(sanoq)