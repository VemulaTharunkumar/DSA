n=int(input())
l=[]

for i in range(n):
    x=input()
    l.append(x)

print("List of strings:",l)

print("Merged string using built-in function:","".join(l))

s=""
for i in l:
    s=s+i

print("Merged string without using built-in function:",s)