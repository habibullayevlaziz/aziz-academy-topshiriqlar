import sys
def hisobla():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    umumiy_oquvchilar = len(input_data) - 1 - n
    print(umumiy_oquvchilar)
if __name__ == "__main__":
    hisobla()