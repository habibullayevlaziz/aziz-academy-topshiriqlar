# INPUT:
# 1-qator: n
# keyingi n qator: x y
# VAZIFA:
# - koordinatalarni tuple (x,y) ko‘rinishida saqlang
# - eng katta x ga ega nuqtani toping
# - agar x teng bo‘lsa, y kichigi yutsin
# OUTPUT: x y
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
best_point = max(points, key=lambda p: (p[0], -p[1]))
print(best_point[0], best_point[1])