line1 = input().split()
line2 = input().split()
dict1 = {}
for word in line1:
    dict1[word] = True
common_words = set()
for word in line2:
    if word in dict1:
        common_words.add(word)
for word in sorted(common_words):
    print(word)