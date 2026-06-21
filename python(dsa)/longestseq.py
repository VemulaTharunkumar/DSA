li=list(map(int,input().split()))
s=set(li)
m=0
st=0
for x in s:
    if x-1 not in s:
        c=1
        while x+c in s:
            c+=1
        if c>m:
            m=c
            st=x
print(m)
print(*range(st,st+m))