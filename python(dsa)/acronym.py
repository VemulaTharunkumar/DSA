"""s=input()
l=list(s.split())
for k in l:
    print(k[0],end="")  """

s=input()
s1=""
for char in s:
    if char==char.upper():
        s1+=char    
print(s1)