d = {}
for _ in range(3):
    fan, baho = input().split()
    baho = int(baho)
    d[fan] = baho
eng_yuqori_fan = max(d, key=d.get)
eng_yuqori_baho = d[eng_yuqori_fan]
print(eng_yuqori_fan, eng_yuqori_baho)