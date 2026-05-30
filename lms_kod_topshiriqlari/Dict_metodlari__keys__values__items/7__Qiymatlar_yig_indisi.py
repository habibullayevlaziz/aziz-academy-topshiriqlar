n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
print(sum(d.values()))    
# n = int(input())
# d = {}
# for _ in range(n):
#     k, v = input().split()
#     d[k] = int(v)
# qiymatlar yig'indisini chiqaring