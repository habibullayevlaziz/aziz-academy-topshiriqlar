n = int(input())
arr = list(map(int, input().split()))
best_num = arr[0]
best_count = 0
for i in range (n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    if count > best_count:
        best_count = count
        best_num = arr[i]
    elif count == best_count:
        if arr[i] < best_num:
            best_num = arr[i]
print(best_num)