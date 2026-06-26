tokens = input().split()
words = sorted({token.lower() for token in tokens if token.isalpha()})
if words:
    print(*words)
else:
    print("BO'SH")