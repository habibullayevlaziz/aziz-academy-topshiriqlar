nums = map(int, input().split())
unique_nums = {x for x in nums}
sorted_nums = sorted(unique_nums)
print(*sorted_nums)

# INPUT: 1 qatorda butun sonlar (space bilan)
# VAZIFA: unikal sonlardan set yasang
# OUTPUT: unikal sonlarni o‘sish tartibida (sorted) space bilan chiqaring
# Masalan: 2 1 2 3 -> 1 2 3
# Eslatma: set comprehension ishlatish mumkin: {x for x in nums}
