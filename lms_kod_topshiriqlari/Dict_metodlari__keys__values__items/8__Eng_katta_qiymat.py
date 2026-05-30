n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
print(max(d.values()))    
# n = int(input())
# d = {}
# for _ in range(n):
#     k, v = input().split()
#     d[k] = int(v)
# eng katta qiymatni chiqaring