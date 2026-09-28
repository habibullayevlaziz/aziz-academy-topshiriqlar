total_sum = 0
while True:
    s = input().strip()
    if s == "stop":
        break
    total_sum += int(s)
print(total_sum)