s = input().strip()
print(s.isalnum() and s.islower() and any(c.isdigit()for c in s))