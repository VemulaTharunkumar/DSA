l=list(map(int,input().split()))
print(sum(l))
print(sum(l)/len(l))
print(min(l))
print(max(l))
try:
    n=int(input("Enter index number:"))
    print(l[n])
except IndexError:
    print("Index is more than list not possible to access")
        