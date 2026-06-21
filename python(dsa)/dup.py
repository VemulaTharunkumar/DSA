li=list(map(int,input().split()))
s=set(li)
print("Using set",s)
print("------------------")


li=list(map(int,input().split()))
l=[]
for x in li:
    if x not in l:
        l.append(x)
print("Without set",l)