words = input().split()
lengths = set(len(word)for word in words)
print(*sorted(lengths))