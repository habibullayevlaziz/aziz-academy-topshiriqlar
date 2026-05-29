secret = 9
while True:
    guess = int(input())
    if guess == secret:
        print("Correct")
        break
    elif guess < secret:
        print("Low")
    else:
        print("High")