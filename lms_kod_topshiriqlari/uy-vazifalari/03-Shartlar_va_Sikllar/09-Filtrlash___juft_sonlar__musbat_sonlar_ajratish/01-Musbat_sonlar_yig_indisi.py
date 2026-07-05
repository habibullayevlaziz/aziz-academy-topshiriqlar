import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    musbat_yigindi = 0
    for i in range(1, n + 1):
        number = int(input_data[i])
        if number > 0:
            musbat_yigindi += number
    print(musbat_yigindi)
if __name__ == '__main__':
    main()