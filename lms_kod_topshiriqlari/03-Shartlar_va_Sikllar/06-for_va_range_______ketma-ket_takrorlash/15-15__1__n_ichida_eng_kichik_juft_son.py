n = int(input())
min_even = None
for i in range(1, n + 1):
    if i % 2 == 0:
        if min_even is None or i < min_even:
            min_even = i
if min_even is not None:
    print(min_even)
else:
    print("No")