# INPUT: 1 qatorda butun sonlar
# VAZIFA: range = max - min ni hisoblang
# OUTPUT: range
numbers = list(map(int, input().split()))
if len(numbers) >  1:
    result = max(numbers) - min(numbers)
else:
    result = 0
print(result)