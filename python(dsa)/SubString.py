def Is(s1,s2):
    l=[]
    k=0
    for i in range(0,len(s2)):
        l.append(s1[i])   
    for j in range(len(s2),len(s1)):
        r="".join(l)
        if r==s2:
            return True
        else:
            l.pop(k)   
            i+=1
            l.append(s1[j])
    return False        
s1=input()
s2=input()
if(Is(s1,s2)):
    print("Substring")
else:
    print("Not a substring")
                         