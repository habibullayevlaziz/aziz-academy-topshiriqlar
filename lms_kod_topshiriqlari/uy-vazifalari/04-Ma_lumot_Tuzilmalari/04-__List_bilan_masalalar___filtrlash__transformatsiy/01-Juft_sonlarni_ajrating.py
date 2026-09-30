nums = map(int,input().split())
evens = [str(x) for x in nums if x % 2 == 0]
print(" ".join(evens))