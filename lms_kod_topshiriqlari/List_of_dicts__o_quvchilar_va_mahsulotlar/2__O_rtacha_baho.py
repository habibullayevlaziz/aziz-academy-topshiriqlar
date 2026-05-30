N = int(input())
scores = []
for _ in range(N):
    name, score = input().split()
    scores.append(int(score))
averege = sum(scores) / N
print(averege)
