n = int(input())
numbers = list(map(int, input().split()))
odd_numbers = [x for x in numbers if x % 2 != 0]
if odd_numbers:
    print(max(odd_numbers))
else:
    print("No")