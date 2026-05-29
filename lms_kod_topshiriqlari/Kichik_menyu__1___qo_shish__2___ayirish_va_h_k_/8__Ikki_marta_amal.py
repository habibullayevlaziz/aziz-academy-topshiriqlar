for _ in range(2):
    son1, son2 = map(int, input().split())
    amal = int(input())
    if amal == 1:
        print(son1 + son2)
    elif amal == 2:
        print(son1 - son2)
    elif amal == 3:
        print(son1 * son2)
    elif amal == 4:
        print(son1 / son2)
oxirgi_amal = input()
if oxirgi_amal == "0":
    print("Exit")