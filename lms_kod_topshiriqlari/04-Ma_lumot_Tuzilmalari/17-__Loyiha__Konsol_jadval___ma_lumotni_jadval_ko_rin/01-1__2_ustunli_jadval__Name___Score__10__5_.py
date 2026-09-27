n = int(input())
print("Name       | Score")
print("-" * 10 + "+" + "-" * 5)
for _ in range(n):
    name, score = input().split()
    score = int(score)
    print(f"{name:<10} | {score:>5}")