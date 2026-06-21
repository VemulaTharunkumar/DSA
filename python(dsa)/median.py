li=list(map(int,input().split()))
li.sort()

n=len(li)

if n%2==1:
    print(li[n//2])
else:
    print((li[n//2-1]+li[n//2])/2)