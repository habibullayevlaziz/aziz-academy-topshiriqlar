th1, lang1, dbg1 = input().split()
th2, lang2, dbg2 = input().split()
theme = th2 if th2 != '-' else th1
lang = lang2 if lang2 != '-' else lang1
debug = dbg2 if dbg2 != '-' else dbg1
print(theme, lang, debug)