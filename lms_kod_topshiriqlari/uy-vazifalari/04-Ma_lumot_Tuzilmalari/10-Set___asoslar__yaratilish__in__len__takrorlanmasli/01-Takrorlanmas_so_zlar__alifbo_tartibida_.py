import sys
words = sorted(set(sys.stdin.read().split()))
print(*words)