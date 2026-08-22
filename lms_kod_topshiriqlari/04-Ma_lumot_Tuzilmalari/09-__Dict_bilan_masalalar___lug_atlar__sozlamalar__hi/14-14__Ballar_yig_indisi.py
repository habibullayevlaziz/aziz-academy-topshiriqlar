# Kodingizni shu yerga yozing
n = int(input())
d = {}
for i in range(n):
    ism, ball = input().split()
    d[ism] = int(ball)
print(sum(d.values()))