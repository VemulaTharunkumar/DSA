records=[
("India",143,7.0),
("China",141,5.2),
("Japan",12,1.1),
("Indonesia",28,5.0),
("Australia",3,2.4),
("South Korea",5,1.7),
("Thailand",7,2.9),
("Malaysia",3,4.3)
]

while True:
    print("\n1.Country wise")
    print("2.Population wise")
    print("3.GDP wise")
    print("4.Country and Population wise")
    print("5.Country and GDP wise")
    print("6.Exit")

    ch=int(input("Enter choice: "))

    match ch:
        case 1:
            res=sorted(records,key=lambda x:x[0])
            print(res)

        case 2:
            res=sorted(records,key=lambda x:x[1])
            print(res)

        case 3:
            res=sorted(records,key=lambda x:x[2])
            print(res)

        case 4:
            res=sorted(records,key=lambda x:(x[0],x[1]))
            print(res)

        case 5:
            res=sorted(records,key=lambda x:(x[0],x[2]))
            print(res)

        case 6:
            print("Exiting...")
            break

        case _:
            print("Invalid Choice")