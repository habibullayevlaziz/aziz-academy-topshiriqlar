numbers = list(map(int, input().split()))
even_numbers = [num for num in numbers if num % 2 == 0]
if even_numbers:
    print(*even_numbers)
else:
    print("BO'SH")