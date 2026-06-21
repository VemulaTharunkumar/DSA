"""given string as i/p, that contains only lower case english alphabets then find & return first non-repeating character.
Ex:-
s = "abacaba" O/p:- c
s = "abc"O/p:- a
s = "ababbaba"O/p:- {None.}
s = "a" O/p:- a."""
s=input()
d={}
for char in s:
    d[char]=d.get(char,0)+1
    
found=False
for y in s:
    if(d.get(y)==1):
        print(y)
        found=True
        break
if not found:
        print("{None}")