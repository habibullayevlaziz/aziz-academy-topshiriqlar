n = int(input())
sonlar_str = input()
sonlar_list = sonlar_str.split()
yigindi = 0
for i in range(n):
    yigindi += int(sonlar_list[i])
print(yigindi)