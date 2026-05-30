n = int(input())
scores = []
for _ in range(n):
    name, score = input().split()
    scores.append(int(score))
x = int(input())
count = scores.count(x)
print(count)
