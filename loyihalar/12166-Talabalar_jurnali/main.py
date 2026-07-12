jurnal = []
while True:
    try:        
        cmd = input().strip()
        if not cmd:
            continue            
        if cmd == 'exit':
            break
        elif cmd.startswith('add '):
            parts = cmd.split()
            if len(parts) >= 3:
                ism = parts[1]
                try:                    
                    ball = int(parts[2])
                except ValueError:
                    print("Xato: ball son bo'lsin")
                    continue
                if ball < 0 or ball > 100:
                    print("Xato: ball 0-100 oralig'ida bo'lsin")
                    continue
                jurnal.append([ism, ball])
                print(f"Yozildi: {ism} — {ball} ball")
            else:
                print("Xato: Format notog'ri. 'add <ism> <ball>' ko'rinishidan yozing.")
        elif cmd == 'list':
            if not jurnal:
                print("Jurnal bo'sh")
            else:
                for i, (ism, ball) in enumerate(jurnal, 1):
                    print(f"{i}. {ism} — {ball} ball")
        elif cmd == 'top':
            if not jurnal:
                print("Jurnal bo'sh")
            else:
                eng_yaxshi = max(jurnal, key=lambda t: t[1])
                print(f"Eng yaxshi: {eng_yaxshi[0]} ({eng_yaxshi[1]} ball)")
        elif cmd.startswith('search '):
            parts = cmd.split()
            qidirilayotgan_ism = parts[1]
            topildi = False
            for ism, ball in jurnal:
                if ism == qidirilayotgan_ism:
                    print(f"Topildi: {ism} — {ball} ball")
                    topildi = True
                    break
            if not topildi:
                print(f"Topilmadi: {qidirilayotgan_ism}")
        elif cmd == 'stat':
            if not jurnal:
                print("Jurnal bo'sh")
            else:
                talabalar_soni = len(jurnal)
                ortacha = round(sum(b for _, b in jurnal) / talabalar_soni, 1)
                print(f"Talabalar: {talabalar_soni} | O'rtacha: {ortacha}")
    except (EOFError, KeyboardInterrupt):
        break
    except Exception as e:
        print(f"Kutilmagan xatolik: {e}")
                    