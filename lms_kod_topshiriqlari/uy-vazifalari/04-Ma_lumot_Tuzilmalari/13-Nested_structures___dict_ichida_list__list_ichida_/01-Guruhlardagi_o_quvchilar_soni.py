import sys
def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())
    for i in range(1, n + 1):
        parts = input_data[i].split()
        if parts:
            print(f"{parts[0]} {len(parts) - 1}")
if __name__ =="__main__":
    solve()