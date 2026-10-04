sonlar = set(map(int, input().split()))
qidiriladigam_sonlar = int(input())
if qidiriladigam_sonlar in sonlar:
    print("Bor")
else:
    print("Yo'q")