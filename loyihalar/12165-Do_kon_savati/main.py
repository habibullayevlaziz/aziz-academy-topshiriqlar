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
                    narx = int(parts[2])
                    savat.append([nom, narx])
                    print(f"Savatga qo'shildi: {nomi} ({narx} so'm)")
                except ValueError:
                    pass
        elif parts[0] == 'list':
            if not savat:
                print("Savat bo'sh")
            else:
                for i, (nom, narx) in enumerate(savat, 1)
                print(f"{i}. {nom} - {narx} so'm")
    except EOFError:
        break