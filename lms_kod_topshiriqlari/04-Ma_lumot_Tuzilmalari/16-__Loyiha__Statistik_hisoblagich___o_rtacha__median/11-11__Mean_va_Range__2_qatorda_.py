# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - mean (2 kasr)
# - range (max-min)
# OUTPUT:
# 1-qator: mean (2 kasr)
# 2-qator: range (int)
numbers = list(map(int, input().split()))
mean_val = sum(numbers) / len(numbers)
range_val = max(numbers) - min(numbers)
print(f"{mean_val:.2f}")
print(range_val)