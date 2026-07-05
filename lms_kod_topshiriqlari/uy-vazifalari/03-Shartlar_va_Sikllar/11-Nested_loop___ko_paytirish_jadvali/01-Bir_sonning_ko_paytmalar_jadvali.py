import sys
def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    n = int(input_data)
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")
if __name__ == "__main__":
    main()