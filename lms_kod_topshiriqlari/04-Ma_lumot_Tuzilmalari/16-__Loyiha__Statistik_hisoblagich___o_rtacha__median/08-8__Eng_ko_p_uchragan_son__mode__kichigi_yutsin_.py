# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - eng ko‘p uchragan sonni toping (mode)
# - agar bir nechta son bir xil ko‘p uchrasa, eng kichigini tanlang
# OUTPUT: mode
# Eslatma: dict (hisoblagich) ishlatish mumkin
numbers = list(map(int, input().split()))
most_comman = min(set(numbers), key=lambda x: (-numbers.count(x), x))
print(most_comman)