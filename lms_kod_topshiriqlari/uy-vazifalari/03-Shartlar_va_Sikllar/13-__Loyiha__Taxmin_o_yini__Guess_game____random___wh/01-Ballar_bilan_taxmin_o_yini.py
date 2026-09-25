secret = int(input())
score = 100
while True:
    guess = int(input())
    if guess > secret:
            print("KATTA")
            score = max(0, score - 10)
    elif guess < secret:
        print("KICHIK")
        score = max(0, score - 10)
    else:
        print("TOPDINGIZ")
        print(f"Ball: {score}")
        break