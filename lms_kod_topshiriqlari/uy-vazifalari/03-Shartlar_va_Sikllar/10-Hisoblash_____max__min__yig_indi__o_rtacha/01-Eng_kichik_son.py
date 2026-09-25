n = int(input())
min_val = int(input())
for i in range(n - 1):
    num = int(input())
    if num < min_val:
        min_val = num
print(min_val)