r = int(input())
attempts = []
for i in range(1, r + 1):
    target = int(input())
    count = 0
    while True:
        count += 1
        if int(input()) == target:
            attempts.append(count)
            break
    print(f"Round {i}: {count} urinish")
print(f"Jami: {sum(attempts)}\nEng yaxshi: {min(attempts)}")
