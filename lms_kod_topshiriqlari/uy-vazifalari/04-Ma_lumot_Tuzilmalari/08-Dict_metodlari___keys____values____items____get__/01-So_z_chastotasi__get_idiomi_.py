s = input().split()
words = {}
for word in s:
    words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print(word, words[word])