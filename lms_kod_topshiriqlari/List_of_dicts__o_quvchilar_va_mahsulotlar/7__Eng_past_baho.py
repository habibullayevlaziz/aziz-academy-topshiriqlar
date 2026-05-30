n = int(input())
name, score = input().split()
min_score = int(score)
for _ in range(n - 1):
    name, score = input().split()
    score = int(score)
    if score < min_score:
        min_score = score
print(min_score)