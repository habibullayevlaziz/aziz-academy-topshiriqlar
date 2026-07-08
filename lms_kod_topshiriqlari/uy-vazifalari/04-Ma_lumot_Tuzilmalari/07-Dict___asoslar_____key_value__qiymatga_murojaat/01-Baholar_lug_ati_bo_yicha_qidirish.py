n = int(input())
lugat = {}
for _ in range(n):
    ism, ball = input().split()
    lugat[ism] = ball
qidirilayotgan_ism = input()
print(lugat[qidirilayotgan_ism])