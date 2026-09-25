# INPUT: 1 qatorda butun sonlar
# VAZIFA: unikal sonlar sonini toping (set yordamida)
# OUTPUT: unique_count
numbers = list(map(int, input().split()))
print(len(set(numbers)))