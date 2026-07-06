target = int(input())
max_attempts = int(input())
won = False
for _ in range(max_attempts):
    guess = int(input())
    if guess > target:
        print("KATTA")
    elif guess < target:
        print("KICHIK")
    else:
        print("TOPDINGIZ")
        won = True
        break
if not won:
    print("YUTQAZDINGIZ")