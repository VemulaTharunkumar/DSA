def pivo(a,l,h):
    p=a[h]
    i=l
    for j in range(l,h):
        if a[j]<p:
            t=a[j]
            a[j]=a[i]
            a[i]=t
            i+=1
    t=a[i]
    a[i]=a[h]
    a[h]=t
    return i
    
def kthsma(a,l,h,k):
    res=pivo(a,l,h)
    if res==k-1:
        return a[k-1]
    elif res>k-1:
       return kthsma(a,l,res-1,k)
    else:
       return kthsma(a,res+1,h,k)
a=list(map(int,input("Enter list of elements :").split()))
k=int(input("Enter k :"))
res=kthsma(a,0,len(a)-1,k)
print("Kthsmallest :",res)