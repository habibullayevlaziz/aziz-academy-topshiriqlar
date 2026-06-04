s = input()
digits = {ch for ch in s if ch.isdigit()}
if digits:
    print(*sorted(digits))
else:
    print("BO'SH")