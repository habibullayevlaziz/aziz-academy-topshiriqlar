n = int(input())
skip = int(input())
i = 1
while i <= n:
    if i == skip:
        i += 1
        continue
    print(i)
    i += 1
    
# n = int(input())
# skip = int(input())
# while i<=n, agar i==skip bo'lsa continue qiling.
