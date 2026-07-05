import sys 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    sonlar = [int(x) for x in input_data[1:n+1]]
    if sonlar:
        ayirma = max(sonlar) - min(sonlar)
        print(ayirma)
if __name__ == '__main__':
    main()