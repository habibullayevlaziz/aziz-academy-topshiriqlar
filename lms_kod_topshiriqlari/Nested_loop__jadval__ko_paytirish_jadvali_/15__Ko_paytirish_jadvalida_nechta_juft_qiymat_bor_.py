n, m = map(int, input().split())
odd_i = (n + 1) // 2
odd_j = (m + 1) // 2
total = n * m
odd = odd_i * odd_j
print(total - odd)
    
