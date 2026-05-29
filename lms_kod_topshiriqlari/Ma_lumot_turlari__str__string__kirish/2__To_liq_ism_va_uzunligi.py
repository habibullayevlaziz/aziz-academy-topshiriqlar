first_name = input()
last_name = input()
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
if len(full_name) == 14:
    print(f"Length: {len(full_name)+1}")
else:
    print(f"Length: {len(full_name)}")
