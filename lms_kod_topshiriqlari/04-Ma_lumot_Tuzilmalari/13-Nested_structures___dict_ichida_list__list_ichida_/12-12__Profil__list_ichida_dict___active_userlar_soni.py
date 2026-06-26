n = int(input().strip())
active_count = 0
for _ in range(n):
    username, active = input().split()
    if active == '1':
        active_count += 1
print(active_count)