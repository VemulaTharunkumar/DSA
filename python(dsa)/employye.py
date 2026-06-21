n = int(input())
d={}
for i in range(n):
    
    name=input()
    job=input()
    salary=int(input())
    d[i]={"name":name,"job":job,"salary":salary}
for i in d:
    print("name :",d[i]["name"], " job : ",d[i]["job"]," salary : ",d[i]["salary"])
x=input()
v=d.values()
for i in v:
    if x == i.get("name"):
        print(i)