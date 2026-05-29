secret = 15
while True:
    guess = int(input())
    if guess == secret:
        print("Correct")
        break
    elif abs(secret - guess) >= 5:
        print("Far")
    else:
        print("Close")
