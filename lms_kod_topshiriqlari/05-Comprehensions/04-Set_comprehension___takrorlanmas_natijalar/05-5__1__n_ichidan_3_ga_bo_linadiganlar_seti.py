n = int(input())
divisible_by_3_set = {x for x in range(1, n + 1) if x % 3 == 0}
if not divisible_by_3_set:
    print("BO'SH")
else:
    sorted_numbers = sorted(divisible_by_3_set)
    print(*sorted_numbers)