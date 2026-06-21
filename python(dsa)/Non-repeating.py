def NonRepeating(s):
    i=1
    j=0
    max1=0
    while(i<len(s)):
        if(s[i]==s[i-1]):
            i+=1
        else:
            max1=max(max1,i-j)
            j=i
            i+=1
    max1=max(max1,i-j)
    return max1

s=input()
print(NonRepeating(s))        
              