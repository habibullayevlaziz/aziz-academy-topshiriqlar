N = int(input())
for i in range(1, N + 1):
    qator = []
    for j in range(1, i + 1):
        qator.append(str(i * j))
    print(" ".join(qator))