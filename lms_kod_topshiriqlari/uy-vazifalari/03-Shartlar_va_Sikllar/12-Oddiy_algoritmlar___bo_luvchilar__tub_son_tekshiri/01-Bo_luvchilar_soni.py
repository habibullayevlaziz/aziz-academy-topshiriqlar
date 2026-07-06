import math
n = int(input())
divisors = set()
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)
print(len(divisors))
              