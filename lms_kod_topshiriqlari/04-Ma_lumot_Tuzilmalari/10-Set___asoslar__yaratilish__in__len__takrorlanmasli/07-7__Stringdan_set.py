s = input()
print("{", end="")
for i in range(len(s)):
    print(f"'{s[i]}'", end = "")
    if i != len(s) - 1:
        print(", ", end="")
print("}")
