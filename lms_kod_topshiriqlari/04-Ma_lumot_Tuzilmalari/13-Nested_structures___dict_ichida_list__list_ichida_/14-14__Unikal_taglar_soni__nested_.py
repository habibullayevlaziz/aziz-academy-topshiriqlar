n = int(input().strip())
unique_tags = set()
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    for tag in tags:
        unique_tags.add(tag)
print(len(unique_tags))