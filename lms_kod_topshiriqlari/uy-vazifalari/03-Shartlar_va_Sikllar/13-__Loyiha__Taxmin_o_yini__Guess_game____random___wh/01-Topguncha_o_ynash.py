target = int(input())
attempts = 0
while True:
    guess = int(input())
    attempts += 1
    if guess > target:
        print("KATTA")
    elif guess < target:
        print("KICHIK")
    else:
        print("TOPDINGIZ")
        print(f"Urinishlar: {attempts}")
        break