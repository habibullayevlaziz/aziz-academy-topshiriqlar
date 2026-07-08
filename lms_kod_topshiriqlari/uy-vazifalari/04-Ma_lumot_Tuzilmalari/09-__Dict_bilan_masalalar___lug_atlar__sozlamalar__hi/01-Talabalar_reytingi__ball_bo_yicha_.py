n = int(input())
natijalar = []
for _ in range(n):
    ism, ball = input().split()
    natijalar.append((ism, int(ball)))
for ism, ball in sorted(natijalar, key=lambda x: x[1], reverse=True):
    print(ism, ball)
