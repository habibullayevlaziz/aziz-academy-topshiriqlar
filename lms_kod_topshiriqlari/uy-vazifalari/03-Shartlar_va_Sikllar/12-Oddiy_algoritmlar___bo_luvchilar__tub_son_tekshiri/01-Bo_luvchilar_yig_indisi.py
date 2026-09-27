n = int(input())
yigindi = 0
i = 1
while i * i <= n:
    if n % i == 0:
        if i * i == n:
            yigindi += i
        else:
            yigindi += i + (n // i)
    i += 1
print(yigindi)