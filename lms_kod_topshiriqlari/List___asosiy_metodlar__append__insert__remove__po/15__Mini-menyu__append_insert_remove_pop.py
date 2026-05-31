lst = []
while True:
    cmd = input().split()
    if cmd[0] == "stop":
        break
    elif cmd[0] == "append":
        lst.append(int(cmd[1]))
    elif cmd[0] == "insert":
        i = int(cmd[1])
        x = int(cmd[2])
        lst.insert(i, x)
    elif cmd[0] == "remove":
        x = int(cmd[1])
        if x in lst:
            lst.remove(x)
    elif cmd[0] == "pop":
            i = int(cmd[1])
            if 0 <= i < len(lst):
                lst.pop(i)
print(lst)