n = int(input())
sum_of_divisors = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum_of_divisors += i
print(sum_of_divisors)
