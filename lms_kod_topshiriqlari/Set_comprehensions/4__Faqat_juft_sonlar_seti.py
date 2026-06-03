numbers = list(map(int, input().split()))
even_numbers_set = {x for x in numbers if x % 2 == 0}
if not even_numbers_set:
    print("BO'SH")
else:
    sorted_even = sorted(even_numbers_set)
    print(*sorted_even)
