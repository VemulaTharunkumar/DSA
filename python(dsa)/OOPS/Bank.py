class InsufficientException(Exception):
    pass
class Bank:
    id=100
    def __init__(self,name):
        Bank.id+=1
        self.name=name
        self.acno=Bank.id
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdrawl(self,amount):
        try:
            if amount>self.balance:
                raise InsufficientException
            else:    
                self.balance-=amount
        except InsufficientException:
            print("--Insufficient Balance--")        
    def display(self):
        print("Ac_no:",Bank.id)
        print("Name :",self.name)
        print("Balance :",self.balance)
    def check_balance(self):
        print("Balance",self.balance)    
print("Enter Account Details:")
d={}
while True:
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdrawl")
    print("4.Display")
    print("5.Balance")
    print("6.exit")
    x=int(input())
    match x:
        case 1:
            c=input()
            b=Bank(c)
            d[Bank.id]=b
            print("Account Details:",c,b.id)
        case 2:
            try:
                w=int(input("Enter account number :"))
                a=int(input("Enter amount :"))
                d[w].deposit(a)
            except KeyError as e:
                print("*No such Account exists*")    
        case 3:
            try:
                w=int(input("Enter account number :"))
                a=int(input("Enter amount :"))
                d[w].withdrawl(a)
            except KeyError as e:
                print("*No such Account exists*")
        case 4:
            try:
                w=int(input("Enter ac number:"))
                d[w].display()
            except KeyError as e:
                print("*No such Account exists*")    
        case 5:
            try:
                w=int(input("Enter ac number:"))
                d[w].check_balance()
            except KeyError as e:
                print("*No such account exists*")    
        case 6:
            exit()
        case _:
            print("Invalid choice")                    
            
            
        
                
            
            