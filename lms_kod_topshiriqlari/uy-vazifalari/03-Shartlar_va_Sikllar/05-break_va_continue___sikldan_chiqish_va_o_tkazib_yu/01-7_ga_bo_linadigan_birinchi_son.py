n = int(input())
found = False
for _ in range(n):
    son = int(input())
    if son % 7 == 0:
        print(son)
        found = True
        break
if not found:
    print("yo'q")