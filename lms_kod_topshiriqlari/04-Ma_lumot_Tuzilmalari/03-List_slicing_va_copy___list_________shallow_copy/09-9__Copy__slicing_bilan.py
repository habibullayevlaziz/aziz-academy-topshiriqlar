n = int(input())
a = list(map(int, input().split()))
b = a[:]
b[0] = 99
print(a)
print(b)

# n = int(input())
# a = list(map(int, input().split()))
# b ni slicing bilan copy qiling.
# b[0] ni 99 ga o'zgartiring.
# a va b ni alohida chiqaring.