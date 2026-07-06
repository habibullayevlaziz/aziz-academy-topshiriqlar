import sys
print(*dict.fromkeys(sys.stdin.read().split()))