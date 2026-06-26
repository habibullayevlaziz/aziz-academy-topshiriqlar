a, b = map(int, input().split())
if b == 0:
    print("Error")
elif a < 0 or b < 0:
    print("Invalid")
else:
    print(a / b)