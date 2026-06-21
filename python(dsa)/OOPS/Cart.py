class Cart:
    cart=[]
    def __init__(self):
        self.d={}
        self.n=int(input("Enter no of items available :"))
        for i in range(self.n):
            self.item=input("Item name:")
            self.type=input("Item Type:")
            self.price=int(input("Item price :"))
            self.d[self.item]=[self.type,self.price]
        print(self.d)    
    
    def add_item(self):
        for key in self.d:
            print(key,self.d[key][1])
        self.item=input("Enter item to add in cart :")
        if self.item in self.d:
            Cart.cart.append(self.item)
            print("Item added")
        else:
            print("Item not Available")
        print("Cart",Cart.cart)  
    
    def remove(self):
        r=input("Enter item to remove from cart:")
        if r not in Cart.cart:
           print("Item not in cart")
        else:
            Cart.cart.remove(r) 
            print("Item Removed")
            print("Cart Items:",Cart.cart)         
        
    def order(self):
        s=input(f"Are you sure want to order {Cart.cart}")
        self.total=0
        if s.lower() in ["y","yes"]:
            for i in Cart.cart:                
                self.total+=self.d[i][1]
                print(f"Item :{i}")
                print(f"Price :{self.d[i][1]}")
                print(f"Type :{self.d[i][0]}")
                print("---------------------------------")
            print("Total Bill:",self.total)
        else:
            print("Order Cancelled")        
b=Cart()
while True:
    x=int(input("Enter Choice:"))
    match x:
        case 1:     
            while True:
                b.add_item()
                ch=input("Add more items?(y/n) :")
                if ch.lower()=="n":
                    break
        case 2:
            while True:
                b.remove()
                ch=input("Remove one more item:{y/n}:")
                if ch.lower()=="n":
                    break
        case 3:
            b.order()
            
        case _:
            print("Invalid Choice")                    

                
                
                
                
            
            