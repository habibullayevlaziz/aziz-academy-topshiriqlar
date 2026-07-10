import sys
def solve():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    n = int(lines[0].strip())
    names = [lines[i].strip() for i in range(1, n + 1) if lines[i].strip()]
    max_len = max(len(name) for name in names)
    for name in names:
        print(f"{name:<{max_len}}|")
if __name__ == "__main__":
    solve()