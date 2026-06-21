n=list(map(int,input().split()))
n.sort()
longest=1
c=1
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        continue
    if n[i]+1==n[i+1]:
        c+=1
    else:
        c=1
    longest=max(longest,c)
print(longest)