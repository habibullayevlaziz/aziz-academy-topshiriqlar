char_to_count = input()
text = input()
counter = 0
for char in text:
    if char == char_to_count:
        counter += 1
print(counter)