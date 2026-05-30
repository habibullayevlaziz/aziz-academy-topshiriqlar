n = int(input().strip())
max_tags = -1
best_user = ""
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    if k > max_tags:
        max_tags = k
        best_user = username
print(best_user)


