# Avtobusda yo'lovchilar sonini hisoblash
# Kurs: IT Dasturlash
# Mavzu: for sikli va range()
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
for i in range(5):
    chiqdi, tushdi = map(int, input().split())
    n = n - chiqdi + tushdi
print(n)