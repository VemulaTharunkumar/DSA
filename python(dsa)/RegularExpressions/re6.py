import re
s = input()
p = r"\b[gG]\w*\b|\b\w*[gG]\b"
print(re.findall(p, s))