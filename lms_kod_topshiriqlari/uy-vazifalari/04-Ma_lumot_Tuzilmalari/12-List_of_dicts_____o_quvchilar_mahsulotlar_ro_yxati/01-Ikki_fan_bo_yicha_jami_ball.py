n = int(input())
for _ in range(n):
    line = input().split()
    name = line[0]
    math_score = int(line[1])
    physics_score = int(line[2])
    total_score = math_score + physics_score
    print(f"{name} {total_score}")