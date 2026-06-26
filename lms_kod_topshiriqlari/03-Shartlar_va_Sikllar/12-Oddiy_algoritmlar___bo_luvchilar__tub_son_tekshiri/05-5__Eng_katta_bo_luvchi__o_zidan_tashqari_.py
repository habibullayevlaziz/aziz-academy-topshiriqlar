n = int(input())
largest = 0
for i in range(1, n):
    if n % i == 0:
        largest = i
print(largest)
       