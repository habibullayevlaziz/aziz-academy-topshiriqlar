words = input().split()
unique_words = {}
for word in words:
    unique_words[word] = True
print(len(unique_words))