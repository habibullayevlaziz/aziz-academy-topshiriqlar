import sys
def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    if a == 1 and b == 1:
        print(1)
    else:
        print(a + b)
if __name__ == '__main__':
    main()