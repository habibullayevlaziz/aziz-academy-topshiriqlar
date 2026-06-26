numbers = list(map(int, input().split()))
musbat_sonlar = [num for num in numbers if num > 0]
if musbat_sonlar:
    print(*musbat_sonlar)
else:
    print("BO'SH")
