n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
yangi_d = {k: v * 2 for k, v in d.items()} 
print(yangi_d)
# n = int(input())
# d = {}
# for _ in range(n):
#     k, v = input().split()
#     d[k] = int(v)
# qiymatlarni 2 ga ko'paytirib yangi dict chiqaring