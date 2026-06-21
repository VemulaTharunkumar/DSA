li=list(map(int,input().split()))
count=1
li.sort()
for i in range(1,len(li)):
        if li[i-1]!=li[i]:
            count+=1
if count==len(li):
    print(True)
else:
    print(False)