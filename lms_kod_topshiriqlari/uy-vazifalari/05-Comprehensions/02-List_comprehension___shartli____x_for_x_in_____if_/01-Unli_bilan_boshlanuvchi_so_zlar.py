import sys
def solve():
    words = sys.stdin.read().split()
    if not words:
        return
    result = [w for w in words if w[0] in "aeioue"]
    print(result)
if __name__ == "__main__":
    solve()