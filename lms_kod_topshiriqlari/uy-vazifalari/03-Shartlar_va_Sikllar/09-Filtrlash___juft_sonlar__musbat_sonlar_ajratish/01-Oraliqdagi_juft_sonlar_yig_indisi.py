A = int(input())
B = int(input())
yigindi = 0
for son in range(A, B + 1):
    if son % 2 == 0:
        yigindi += son
print(yigindi)