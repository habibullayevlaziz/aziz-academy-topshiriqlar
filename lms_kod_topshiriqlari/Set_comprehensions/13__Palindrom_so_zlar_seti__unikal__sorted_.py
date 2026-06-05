words = input().split()
palindromes = sorted({
    word.lower()
    for word in words
    if word.lower() == word.lower()[::-1]
})
if palindromes:
    print(*palindromes)
else:
    print("BO'SH")