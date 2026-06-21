import re
s = input("Enter the string: ")
res = re.findall(r"\ba\w*", s, re.IGNORECASE)
print(res)