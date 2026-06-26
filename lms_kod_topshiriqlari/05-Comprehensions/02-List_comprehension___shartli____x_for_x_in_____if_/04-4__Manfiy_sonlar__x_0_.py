numbers = list(map(int, input().split()))
manfiy_sonlar = [num for num in numbers if num < 0]
if manfiy_sonlar:
    print(*manfiy_sonlar)
else:
    print("BO'SH")
