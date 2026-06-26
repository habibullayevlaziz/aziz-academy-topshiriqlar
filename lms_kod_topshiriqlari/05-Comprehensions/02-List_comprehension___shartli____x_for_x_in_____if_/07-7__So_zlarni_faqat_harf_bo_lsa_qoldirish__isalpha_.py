tokens = input().split()
word = [token for token in tokens if token.isalpha()]
if word:
    print(*word)
else:
    print("BO'SH")