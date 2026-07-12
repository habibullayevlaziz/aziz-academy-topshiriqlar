savat = []
while True:
    try:
        cmd = input().strip()
        if not cmd:
            comtinue
        is cmd == 'exit':
            break
        parts cmd.split()
        if not parts:
            continue
        if parts[0] == 'add':
            if len(parts) >= 3:
                nom = parts[1]
                try:
                    