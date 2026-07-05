import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    musbat_lar_soni = 0
    for i in range(1, n + 1):
        number = int(input_data[i])
        if number > 0:
            musbat_lar_soni += 1
    print(musbat_lar_soni)
if __name__ == '__main__':
    main()