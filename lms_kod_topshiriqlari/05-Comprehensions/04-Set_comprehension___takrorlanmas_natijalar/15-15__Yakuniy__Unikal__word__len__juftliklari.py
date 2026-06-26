words = input().split()
pairs = {
    (word.lower(), len(word.lower()))
    for word in words
}
pairs = sorted(pairs)
print(len(pairs))
for word, length in pairs:
    print(f"{word}:{length}")