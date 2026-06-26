n = int(input())
summa = 0
for i in range(1, n):
    if n % i == 0:
        summa += i
if summa == n:
    print("Perfect")
else:
    print("Not Perfect")