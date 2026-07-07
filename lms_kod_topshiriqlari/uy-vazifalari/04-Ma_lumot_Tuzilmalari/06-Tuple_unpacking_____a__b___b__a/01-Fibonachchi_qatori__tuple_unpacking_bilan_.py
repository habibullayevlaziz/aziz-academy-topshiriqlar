n = int(input())
fib_numbers = []
a, b = 0, 1
for _ in range(n):
    fib_numbers.append(str(a))
    a, b = b, a + b
print(" ".join(fib_numbers))