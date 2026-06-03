numbers = list(map(int, input().split()))
squares_set = {x**2 for x in numbers}
sorted_squares = sorted(squares_set)
print(*sorted_squares)

# INPUT: 1 qatorda butun sonlar
# VAZIFA: har bir sonning kvadratini setga oling (unikal bo‘ladi)
# OUTPUT: kvadratlarni sorted qilib chiqaring
# Masalan: -2 2 3 -> 4 9
