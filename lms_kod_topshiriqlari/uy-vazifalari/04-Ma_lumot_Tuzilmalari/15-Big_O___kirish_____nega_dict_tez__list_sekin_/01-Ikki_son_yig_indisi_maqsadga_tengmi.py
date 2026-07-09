sonlar = list(map(int, input().split()))
target = int(input())
print("Ha" if any(target - x in sonlar[:i] for i, x in enumerate(sonlar)) else "Yoq")
