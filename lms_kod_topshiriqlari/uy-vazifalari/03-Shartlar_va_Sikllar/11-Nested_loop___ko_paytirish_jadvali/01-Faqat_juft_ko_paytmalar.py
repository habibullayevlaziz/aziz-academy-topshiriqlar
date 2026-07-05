import sys
def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    n = int(input_data)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 2 or j == 2:
                print(f"{i} x {j} = {i * j}")
if __name__ == "__main__":
    main()