n = int(input())
malumotlar = []
for _ in range(n):
    ism, ball = input().split()
    malumotlar.append((ism, int(ball)))
malumotlar.sort(key=lambda x: x[1], reverse=True)
for ism, ball in malumotlar:
    print(f"{ism} {ball}")