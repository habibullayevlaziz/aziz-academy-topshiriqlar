n = int(input())
divisors = set()
i = 1
while i * i <= n:
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)
    i += 1
print(*sorted(divisors))