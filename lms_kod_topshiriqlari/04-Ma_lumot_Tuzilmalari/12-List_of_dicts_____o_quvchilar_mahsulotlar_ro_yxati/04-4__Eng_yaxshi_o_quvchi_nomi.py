n = int(input())
max_score = -1
max_namae = ""
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score > max_score:
        max_score = score
        max_name = name
print(max_name)
