n = int(input())
numbers = list(map(int, input().split()))
total = 0 
for num in numbers:
    if num > 10:
        total += num        
print(total)