katta_kolleksiya = set(input().split())
tekshiriladiganlar = input().split()
javob = sum(1 for x in tekshiriladiganlar if x in katta_kolleksiya)
print(javob)