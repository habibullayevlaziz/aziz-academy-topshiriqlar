s = input()
letters = {}
for harf in s:
    if harf not in letters:
        letters[harf] = 1
    else:
        letters[harf] += 1
for harf in letters:
    print(harf, letters[harf])