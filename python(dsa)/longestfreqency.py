"""3) you are given a string which is a collation of words, now find max length word, if 2 or more words have same max length then return 1 st one.
Ex:- s = "The quick brown fox"
O/p:- quick"""
n=list(input().split())
m=0
d={}
for x in n:
    d[x]=len(x)

m=max(d.values())
for k in reversed(d):
    if d.get(k)==m:
        print(k) 
        break  