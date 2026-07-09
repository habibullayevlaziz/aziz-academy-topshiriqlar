n = int(input())
winner, max_len = "", -1
for _ in range(n):
    data = input().split()
    if len(data) > max_len:
        winner, max_len = data[0], len(data)
print(winner)