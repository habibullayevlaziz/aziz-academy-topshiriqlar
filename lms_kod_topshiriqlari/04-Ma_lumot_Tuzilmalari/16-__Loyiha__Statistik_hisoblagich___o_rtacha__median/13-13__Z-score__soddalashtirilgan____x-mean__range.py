# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - mean va range (max-min) ni toping
# - har bir son uchun z = (x-mean)/range ni hisoblang
# - agar range==0 bo‘lsa, hamma z = 0.00
# OUTPUT: z qiymatlarini 2 kasr bilan space orqali chiqaring
numbers = list(map(int, input().split()))
mean_val = sum(numbers) / len(numbers)
range_val = max(numbers) - min(numbers)
if range_val == 0:
    result = ["0.00" for _ in numbers]
else:
    result = [f"{(x - mean_val) / range_val:.2f}" for x in numbers]
print(" ".join(result))