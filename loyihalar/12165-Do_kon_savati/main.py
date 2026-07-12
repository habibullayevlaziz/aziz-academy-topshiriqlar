savat = []
while True:
    try:
        cmd = input().strip()
        if not cmd:
            continue
        if cmd == 'exit':
            break
        parts = cmd.split()
        if not parts:
            continue
        if parts[0] == 'add':
            if len(parts) >= 3:
                nom = parts[1]
                try:
                    narx = int(parts[2])
                    savat.append([nom, narx])
                    print(f"Savatga qo'shildi: {nom} ({narx} so'm)")
                except ValueError:
                    pass
        elif parts[0] == 'list':
            if not savat:
                print("Savat bo'sh")
            else:
                for i, (nom, narx) in enumerate(savat, 1):
                    print(f"{i}. {nom} — {narx} so'm")
        elif parts[0] == 'remove':
            if len(parts) >= 2:
                try:
                    idx = int(parts[1]) - 1
                    if 0 <= idx < len(savat):
                        nom = savat[idx][0]
                        savat.pop(idx)
                        print(f"O'chirildi: {nom}")
                    else:
                        print("Xato: bunday mahsulot yo'q")                        
                except (ValueError, IndexError):
                    print("Xato: raqam kiriting")
        elif parts[0] == 'total':
                    mahsulot_soni = len(savat)
                    jami_narx = sum(narx for _, narx in savat)
                    print(f"Jami: {mahsulot_soni} ta mahsulot, {jami_narx} so'm")
    except EOFError:
        break