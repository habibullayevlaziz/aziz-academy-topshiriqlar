A = set(input().strip().split())
B = set(input().strip().split())
common_names = A.intersection(B)
print(len(common_names))
for name in sorted(common_names):
    print(name)

         
