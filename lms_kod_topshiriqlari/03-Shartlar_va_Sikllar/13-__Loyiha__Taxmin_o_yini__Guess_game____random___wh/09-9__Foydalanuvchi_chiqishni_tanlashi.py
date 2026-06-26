secret = 3
while True:
    guess = int(input())
    if guess == 0:
        print("Exit")
        break
    elif guess == secret:
        print("Correct")
        break
    elif guess < secret:
        print("Low")
    else:
        print("High")