
cnt = 0
while True:
    s = input()
    if s == "0":
        break
    if " " in s:
        cnt += 1
print(cnt)        
