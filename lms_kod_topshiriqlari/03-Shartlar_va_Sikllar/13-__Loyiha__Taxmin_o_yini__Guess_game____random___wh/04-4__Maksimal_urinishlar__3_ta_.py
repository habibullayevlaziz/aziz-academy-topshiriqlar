yashirin = 8
topildi = False
for i in range(3):
    a = int(input())
    if a == yashirin:
        topildi = True
        break
else:
    print("Game Over")
if topildi:
    print("Correct")