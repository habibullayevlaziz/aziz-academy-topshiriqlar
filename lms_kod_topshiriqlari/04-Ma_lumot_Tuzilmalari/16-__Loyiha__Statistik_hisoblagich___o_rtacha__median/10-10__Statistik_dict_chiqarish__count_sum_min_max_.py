# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# stats = {'count':..., 'sum':..., 'min':..., 'max':...} ko‘rinishida dict tuzing
# OUTPUT: dict ni print qiling
# DIQQAT: qiymatlar int bo‘lsin
numbers = list(map(int, input().split()))
stats = {
    'count': len(numbers),
    'sum': sum(numbers),
    'min': min(numbers),
    'max': max(numbers),
}
print(stats)