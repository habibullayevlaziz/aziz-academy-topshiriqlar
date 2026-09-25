n = int(input())
primes = []
for num in range(2, n + 1):
    is_prime = True
    limit = int(num ** 0.5) + 1
    for i in range(2, limit):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
            primes.append(num)
print(*primes)