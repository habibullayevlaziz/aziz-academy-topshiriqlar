n = n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for key, value in d.items():
    print(key, value)

# n = int(input())
# d = {}
# for _ in range(n):
#     k, v = input().split()
#     d[k] = int(v)
# k va v qilib chiqaring