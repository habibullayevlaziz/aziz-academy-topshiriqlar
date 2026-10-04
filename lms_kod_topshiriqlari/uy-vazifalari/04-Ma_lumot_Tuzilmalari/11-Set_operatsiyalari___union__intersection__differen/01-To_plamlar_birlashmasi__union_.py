set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
birlashma = sorted(set1 | set2)
print(*birlashma)