import sys
def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    n = int(input_data)
    for i in range(1, n + 1):
        print(f"{i} * {i} = {i * i}")
if __name__ == "__main__":
    main()