n = int(input())
musbatlar = [x for _ in range(n) if (x := int(input())) > 0]
print(sum(musbatlar) // len(musbatlar) if musbatlar else 0)