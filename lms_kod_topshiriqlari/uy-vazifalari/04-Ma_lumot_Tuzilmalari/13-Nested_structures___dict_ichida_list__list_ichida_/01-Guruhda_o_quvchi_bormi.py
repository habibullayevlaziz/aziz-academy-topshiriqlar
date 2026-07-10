import sys
def solve():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    n = int(lines[0].strip())
    groups = {p[0]: set(p[1:]) for line in lines[1:n+1] if (p := line.split())}
    query = lines[n+1].split()
    if len(query) >= 2:
        g_id, name = query[0], query[1]
        print("Ha" if g_id in groups and name in groups[g_id] else "Yoq")
if __name__ == "__main__":
    solve()