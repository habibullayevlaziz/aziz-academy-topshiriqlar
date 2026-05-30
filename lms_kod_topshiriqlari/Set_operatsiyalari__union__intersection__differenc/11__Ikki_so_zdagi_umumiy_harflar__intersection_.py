a = input().strip()
b = input().strip()
common_chars = set(a).intersection(set(b))
if not common_chars:
    print("BO'SH")
else:
    result = sorted(common_chars)
    print("".join(result))