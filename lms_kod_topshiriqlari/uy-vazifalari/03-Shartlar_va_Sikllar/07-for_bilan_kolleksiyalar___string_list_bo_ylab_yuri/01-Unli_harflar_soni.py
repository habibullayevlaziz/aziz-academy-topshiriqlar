text = input()
vowels = "aeiouAEIOU"
counter = 0
for char in text:
    if char in vowels:
        counter += 1
print(counter)