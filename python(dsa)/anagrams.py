d = {}
l=input().split()
for word in l:
    key="".join(sorted(word))
    if key not in d:
        d[key]=[word]
    else:
        d[key].append(word)

print(d)