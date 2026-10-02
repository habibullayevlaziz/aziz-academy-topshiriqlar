n = int(input())
d = {}
for i in range(n):
    ism, baho = input().split()
    d[ism] = int(baho)
eng_yaxshi_ism = None
eng_yuqori_baho = -1
for ism, baho in d.items():
    if baho > eng_yuqori_baho:
        eng_yuqori_baho = baho
        eng_yaxshi_ism = ism
    elif baho == eng_yuqori_baho:
        if eng_yaxshi_ism is None or ism < eng_yaxshi_ism:
            eng_yaxshi_ism = ism
print(f"{eng_yaxshi_ism} {eng_yuqori_baho}")