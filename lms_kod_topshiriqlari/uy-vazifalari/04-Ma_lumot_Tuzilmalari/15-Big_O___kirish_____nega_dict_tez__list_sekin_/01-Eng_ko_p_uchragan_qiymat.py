from collections import Counter
elementlar = input().split()
hisob = Counter(elementlar)
javob = min(hisob.keys(), key=lambda x: (-hisob[x], x))
print(javob)