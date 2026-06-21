s = set()

while True:
    print("\n1. Check Empty")
    print("2. Add Element")
    print("3. Remove Element")
    print("4. Display Set")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    match ch:
        case 1:
            if len(s) == 0:
                print("Set is empty")
            else:
                print("Set is not empty")

        case 2:
            x = int(input("Enter element to add: "))
            s.add(x)
            print("Element added")

        case 3:
            x = int(input("Enter element to remove: "))
            if x in s:
                s.remove(x)
                print("Element removed")
            else:
                print("Element not found")

        case 4:
            print("Set:", s)

        case 5:
            print("Exiting...")
            break

        case _:
            print("Invalid choice")