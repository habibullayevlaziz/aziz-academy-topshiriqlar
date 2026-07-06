target = int(input())
wrong = 0
while True:
    guess = int(input())
    if guess == target:
        print("TOPDINGIZ")
        print(f"Ball: {max(0, 100 - wrong * 10)}")
        break
    print("KATTA" if guess > target else "KICHIK")
    wrong += 1