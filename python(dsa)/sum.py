n=int(input())

l=[]

for i in range(n):
    x=int(input())
    l.append(x)
t=tuple(l)
print("Tuple:",t)
print("Sum using built-in function:",sum(t))
#------------------------------------------------------------
s=0
for i in t:
    s=s+i

print("Sum without using built-in function:",s)