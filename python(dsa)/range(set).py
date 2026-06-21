set1=set(map(int,input().split()))
print("With built-in",max(set1),min(set1),max(set1)-min(set1))

print("--------------------------------------")

li=set(map(int,input().split()))
max=float('-inf')
min=float('inf')
for x in li:
    if x>max:
        max=x
for x in li: 
    if x<min:
        min=x
print("Without built-in",max,min,max-min)