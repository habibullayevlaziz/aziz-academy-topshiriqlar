def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if is_prime(n):
        count += 1
print(count)