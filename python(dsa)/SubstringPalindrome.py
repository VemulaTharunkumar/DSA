def Palindrome(l):
    i=0
    j=len(l)-1
    while(i<j):
        if l[i]!=l[j]:
            return False
        else:
            i+=1
            j-=1
    return True

def Sub(l):
    r=[]
    p=[]
    for i in range(0,len(l)):
        r=[l[i]]
        for j in range(i+1,len(l)):
            r.append(l[j])
            if(Palindrome(r)):
                p.append(r[:])
            else:
                continue
    return p        
            
l=input()
l=Sub(l)
print(l)                            
            