a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))
umumiy = a & b & c
natija = sorted(umumiy)
print(*natija)