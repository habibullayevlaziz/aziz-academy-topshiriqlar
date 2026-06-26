text = input()
result = ""
for ch in text:
    if ch.isdigit():
        result += ch
if result == "":
    print("BO'SH")
else:
    print(result)