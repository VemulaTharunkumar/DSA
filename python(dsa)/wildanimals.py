n=int(input())
l=[]

for i in range(n):
    animal=input()
    l.append(animal)

x=input()

print("List of wild animals:",l)
print("Count using built-in function:",l.count(x))

c=0
for i in l:
    if i==x:
        c+=1

print("Count without using built-in function:",c)