ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()
allowed = ids.difference(banned)
if not allowed:
    print("BO'SH")
else:
    result = sorted(allowed)
    print(*(result))