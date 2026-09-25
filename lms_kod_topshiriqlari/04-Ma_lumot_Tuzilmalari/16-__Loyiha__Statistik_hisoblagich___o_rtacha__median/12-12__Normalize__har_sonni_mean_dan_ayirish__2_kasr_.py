# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - mean hisoblang
# - har bir son uchun (x - mean) ni hisoblab ro‘yxat qiling
# OUTPUT: natijalarni 2 kasr bilan space orqali chiqaring
# Masalan: 1 2 3 -> -1.00 0.00 1.00
numbers = list(map(int, input().split()))
mean_val = sum(numbers) / len(numbers)
result = [f"{x - mean_val:.2f}" for x in numbers]
print(" ".join(result))