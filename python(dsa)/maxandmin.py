n=list(set(map(int,input().split())))

mn=min(n)
mx=max(n)

n.remove(mn)
n.remove(mx)

print("2nd min =",min(n))
print("2nd max =",max(n))