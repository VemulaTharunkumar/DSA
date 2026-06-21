import re
p = r"[a-zA-Z][a-zA-Z0-9]*@gmail\.com"
s = input("Enter email: ")
if re.fullmatch(p, s):
    print("Valid")
else:
    print("Invalid")