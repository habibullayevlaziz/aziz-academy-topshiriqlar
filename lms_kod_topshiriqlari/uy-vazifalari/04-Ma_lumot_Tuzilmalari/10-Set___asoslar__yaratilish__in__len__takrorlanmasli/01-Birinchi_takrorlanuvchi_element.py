def yechim():
    arr = list(map(int, input().split()))
    korilgan = set()
    for x in arr:
        if x in korilgan:
            print(x)
            return
        korilgan.add(x)
yechim()