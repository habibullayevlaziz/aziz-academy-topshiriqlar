from collections import Counter
import statistics as st
sonlar = list(map(int, input().split()))
ortacha = sum(sonlar) / len(sonlar)
mediana = int(m) if (m := st.median(sonlar)) % 1 == 0 else m
c = Counter(sonlar)
moda = min(sonlar, key=lambda x: (-c[x], x))
print(f"O'rtacha: {ortacha:.1f}\nMediana: {mediana}\nModa: {moda}")