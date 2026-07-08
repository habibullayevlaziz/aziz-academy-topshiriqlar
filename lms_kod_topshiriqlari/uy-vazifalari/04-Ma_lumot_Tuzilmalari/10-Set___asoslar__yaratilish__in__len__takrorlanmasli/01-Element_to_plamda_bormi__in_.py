import sys
lines = sys.stdin.read().splitlines()
if len(lines) >= 2:
    nums = set(lines[0].split())
    target = lines[1].strip()
    print("Bor" if target in nums else "Yo'q")