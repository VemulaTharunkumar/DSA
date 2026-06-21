s=list(input().split())
l=[]
for x in s:
    if(len(x)&1!=0):
        l.append(x[::-1])
    else:
        l.append(x)
s1=" ".join(l)        
print(s1)            
        