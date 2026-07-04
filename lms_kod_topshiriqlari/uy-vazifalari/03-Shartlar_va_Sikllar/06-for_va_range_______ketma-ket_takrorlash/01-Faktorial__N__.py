import sys
import math
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    print(math.factorial(n))
if __name__ == '__main__':
    main()