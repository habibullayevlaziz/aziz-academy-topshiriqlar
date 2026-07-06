import math
n = int(input())
devisors = set()
for i in range(1, int(math.isqrt(n)) + 1):
    if n % i == 0:
        devisors.add(i)
        devisors.add(n // i)
print(*(sorted(devisors)))