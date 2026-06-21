n=int(input())
d={}
c=["name","price","quantity"]
for i in range(n):
    p=list(input().split())
    p[1]=int(p[1])
    p[2]=int(p[2])
    di=dict(zip(c,p))
    d[i]=di
while True:
    c=int(input())
    match c:
        case 1:
            print(dict(sorted(d.items(),key =lambda x:x[1]["name"])))
            print(dict(sorted(d.items(),key =lambda x:x[1]["name"],reverse=True)))
        case 2:
            print(dict(sorted(d.items(),key =lambda x:x[1]["price"])))
            print(dict(sorted(d.items(),key =lambda x:x[1]["price"],reverse=True)))
        case 3:
            print(dict(sorted(d.items(),key =lambda x:x[1]["quantity"])))
            print(dict(sorted(d.items(),key =lambda x:x[1]["quantity"],reverse=True)))
        case 4:
            print(dict(sorted(d.items(),key =lambda x:(x[1]["name"],x[1]["price"]))))
            print(dict(sorted(d.items(),key =lambda x:(x[1]["name"],x[1]["price"]),reverse=True)))
        case 5:
            print(dict(sorted(d.items(),key =lambda x:(x[1]["name"],x[1]["quantity"]))))
            print(dict(sorted(d.items(),key =lambda x:(x[1]["name"],x[1]["quantity"]),reverse=True)))
        case 6:
            print(dict(sorted(d.items(),key =lambda x:(x[1]["price"],x[1]["quantity"]))))
            print(dict(sorted(d.items(),key =lambda x:(x[1]["price"],x[1]["quantity"]),reverse=True)))
        case 7:
            print(dict(sorted(d.items(),key =lambda x:(x[1]["price"],x[1]["quantity"],x[1]["name"]))))
            print(dict(sorted(d.items(),key =lambda x:(x[1]["price"],x[1]["quantity"],x[1]["name"]),reverse=True)))
        case 8:
            exit()