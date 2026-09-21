turi = int(input())
toifasi = int(input())
if turi == 1:
    narx = 1700
elif turi == 2:
    narx1 = 1700 
elif turi == 3:
    narx = 4000
else:
    print("Notog'ri transport")
    exit()
if toifasi == 1:
    yakuniy_narx = narx
elif toifasi == 2:
    yakuniy_narx = narx // 2
elif toifasi == 3:
    yakuniy_narx = 0
else:
    print("Notog'ri toifa")
    exit()
print(yakuniy_narx)