x = input().split()
print("Ha" if len(x) != len(set(x)) else "Yoq")