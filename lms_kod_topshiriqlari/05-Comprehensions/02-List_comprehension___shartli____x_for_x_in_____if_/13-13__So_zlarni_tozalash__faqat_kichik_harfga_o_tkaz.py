words = input().split()
result = []
for word in words:
    word = word.lower()
    if word.startswith("a"):
        result.append(word)
if len(result) == 0:
    print("BO'SH")
else:
    print(" ".join(result))