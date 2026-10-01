n = int(input())
votes = {}
for _ in range(n):
    name = input().strip()
    votes[name] = votes.get(name, 0) + 1
winner = max(votes, key=votes.get)
print(winner)