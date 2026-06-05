text = input().lower()
vowels = sorted(set(ch for ch in text if ch in "aeiou"))
if vowels:
    print(*vowels)
else:
    print("BO'SH")