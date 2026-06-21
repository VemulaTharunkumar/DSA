d={}
n=int(input())
for i in range(n):
    k,v=input().split()
    d[k]=v
try:
    s=input("Enter Student name:")
    print(d[s])
except KeyError:
    print("Student not found")    