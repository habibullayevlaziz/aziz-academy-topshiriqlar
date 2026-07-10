n = int(input())
jami = 0
for _ in range(n):
    majlumot = input().split()
    jami += int(majlumot[1])
print(jami)