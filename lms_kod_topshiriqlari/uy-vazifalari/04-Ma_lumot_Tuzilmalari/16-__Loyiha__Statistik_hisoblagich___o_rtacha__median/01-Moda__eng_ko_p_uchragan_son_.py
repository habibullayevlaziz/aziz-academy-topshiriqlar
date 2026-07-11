from collections import Counter
elementlar = input().split()
javob = Counter(elementlar).most_common(1)[0][0]
print(javob)