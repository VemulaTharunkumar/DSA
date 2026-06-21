"""2) Runlength Encoding (RLE).
given a string of lower case english letter, compress the string by counting consecutive characters.
Ex:- s = aaabbc
O/p:- a3b2c1"""
n=input()
f={}
for x in n:
    f[x]=f.get(x,0)+1
for j in f:
    print(f"{j}{f.get(j)}",end="")
    