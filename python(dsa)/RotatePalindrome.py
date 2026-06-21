def Palindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:
            return False
        else:
            i+=1
            j-=1
    return True    
    
def Rotate(s):
    if(Palindrome(s)):
        return True
    n=len(s)
    k=1
    org=s
    while(k<len(s)):
        t=org
        t=reverse(t,0,k-1)
        t=reverse(t,k,n-1)
        t=reverse(t,0,n-1)
        if Palindrome(t):
            return True
        k+=1
    return False        

def reverse(s,st,e):
    l=list(s)    
    while(st<e):
        temp=l[st]
        l[st]=l[e]
        l[e]=temp
        st+=1
        e-=1
        s="".join(l)
    return s    
s=input()
print(Rotate(s))

    