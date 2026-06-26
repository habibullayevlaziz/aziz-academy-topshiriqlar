A = list(map(int, input().split()))
B = list(map(int, input().split()))
pairs = {(a, b) for a in A for b in B}
pairs = sorted(pairs)
print(len(pairs))
for a, b in pairs:
    print(f"{a},{b}")