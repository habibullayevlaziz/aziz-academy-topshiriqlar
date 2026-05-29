s = input()
new_string = ""
for char in s:
    if char == 'a':
        new_string += '@'
    else:
        new_string += char
print(new_string)