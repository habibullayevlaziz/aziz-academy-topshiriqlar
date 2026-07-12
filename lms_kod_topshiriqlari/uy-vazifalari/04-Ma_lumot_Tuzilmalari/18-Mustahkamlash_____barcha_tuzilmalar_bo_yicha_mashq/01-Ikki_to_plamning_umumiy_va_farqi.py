A = list(map(int, input().split()))
B = list(map(int, input().split()))
set_A = set(A)
set_B = set(B)
kesishma = [x for x in A if x in set_B]
ayirma = [x for x in A if x not in set_B]
print(*(kesishma))
print(*(ayirma))