target = int(input())
k = int(input())
for _ in range(k):
    guess = int(input())
    if guess > target:
        print("KATTA")
    elif guess < target:
        print("KICHIK")
    else:
        print("TOPDINGIZ")