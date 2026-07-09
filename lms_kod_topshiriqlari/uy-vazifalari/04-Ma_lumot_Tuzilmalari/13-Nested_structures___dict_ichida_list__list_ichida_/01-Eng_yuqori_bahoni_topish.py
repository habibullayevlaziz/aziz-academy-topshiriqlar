n = int(input())
winner_name, max_score = "", -1
for _ in range(n):
    data = input().split()
    score = max(map(int, data[1:]))
    if score > max_score:
        winner_name, max_score = data[0], score
print(f"{winner_name} {max_score}")