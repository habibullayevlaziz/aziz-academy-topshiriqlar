username = input()
password = input()
if username == "admin":
    if password == "1234":
        print("Xush kelibsiz")
    else:
        print("Parol xato")
else:
    print("Login topilmadi")