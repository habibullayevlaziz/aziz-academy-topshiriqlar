kirish = input().split()
takror = next((x for i, x in enumerate(kirish) if x in kirish[:i]), "yoq")
print(takror)