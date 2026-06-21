import re
p = r"\br.*o\b"
words = input().split()
li=[]
for word in words:
    if re.findall(p, word):
        li.append(word)
print(li)        
print(len(li))        