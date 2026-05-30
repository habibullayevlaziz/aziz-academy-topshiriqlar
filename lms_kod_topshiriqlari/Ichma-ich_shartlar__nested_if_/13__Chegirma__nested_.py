price = int(input())
if price >= 100:
    if price >= 500:
        price = price * 0.8
    else:
        price = price * 0.9
print(price)

