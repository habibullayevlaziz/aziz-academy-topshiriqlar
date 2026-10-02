n = int(input())
scores = {}
for _ in range(n):
    group, score = input().split()
    score = int(score)
    scores[group] = scores.get(group, 0) + score
for group in sorted(scores.keys()):
    print(f"{group} {scores[group]}")