n = int(input())
if n <= 1:
    print("MUKAMMAL EMAS")
else:
    total_sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total_sum += i
            if i * i != n:
                total_sum += n // i
        i += 1
    if total_sum == n:
        print("MUKAMMAL")
    else:
        print("MUKAMMAL EMAS")
            