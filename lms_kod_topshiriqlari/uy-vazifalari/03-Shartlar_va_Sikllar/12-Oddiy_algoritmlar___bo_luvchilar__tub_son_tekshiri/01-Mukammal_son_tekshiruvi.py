son = int(input())
divisors_sum = sum(i for i in range(1, son) if son % i == 0)
if divisors_sum == son:
    print("MUKAMMAL")
else:
    print("MUKAMMAL EMAS")