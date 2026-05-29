secret = 6
count = 0
while True:
    guess = int(input())
    if guess < 1 or guess > 10:
        print("Invalid")
        continue
    count += 1
    if guess == secret:
        print("Correct")
        break
    elif guess < secret:
        print("Low")
    else:
        print("High")