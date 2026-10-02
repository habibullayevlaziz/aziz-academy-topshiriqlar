numbers = input().split()
seen = set()
found = None
for num in numbers:
    if num in seen:
        found = num
        break
    seen.add(num)
if found is not None:
    print(found)
else:
    print("Yo'q")