emails = input().split()
domains = sorted({
    email.split('@')[1].lower()
    for email in emails
    if '@' in email
})
if domains:
    print(*domains)
else:
    print("BO'SH")