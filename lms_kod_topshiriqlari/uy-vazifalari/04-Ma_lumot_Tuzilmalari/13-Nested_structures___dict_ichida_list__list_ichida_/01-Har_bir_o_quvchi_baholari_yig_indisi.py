n = int(input())
for _ in range(n):
    satr = input().split()
    ism = satr[0]
    ball_yigindisi = sum(int(x) for x in satr[1:])
    print(f"{ism} {ball_yigindisi}")