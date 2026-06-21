li=list(map(int,input().split()))
print([li[x] for x in range(len(li)) if x&1])