elementlar = input().split()
jami_soni = len(elementlar)
unikal_son = len(set(elementlar))
takrorlanganlar = jami_soni - unikal_son
print(takrorlanganlar)