nums = map(int, input().split())
t = int(input())
result = [str(x) for x in nums if x > t]
print(" ".join(result))