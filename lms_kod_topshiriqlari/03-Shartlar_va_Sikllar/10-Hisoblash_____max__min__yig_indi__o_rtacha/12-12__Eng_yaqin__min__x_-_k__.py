n = int(input())
arr = list(map(int, input().split()))
k = int(input())
closest = arr[0]
for num in arr:
    if abs(num - k) < abs(closest - k):
        closest = num
    elif abs (num - k) == abs(closest - k):
        if num < closest:
            closest = num
print(closest)