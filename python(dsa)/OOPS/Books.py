class Book:
    total=0
    def __init__(self,title,author,publisher,price):
        self.__name=title
        self.__author=author
        self.__publisher=publisher
        self.__price=price
    def purchase(self,noc):
        self.__noc=noc
        self.tot=self.__price*self.__noc 
        self.dis=0
        if(self.__noc>0 and self.__noc<=100):
            self.dis=0
        elif self.__noc<=200:
            self.dis=self.tot*0.1
        elif self.__noc<=300:
            self.dis=self.tot*0.2
        elif self.__noc<=400:
            self.dis=self.tot*0.4
        else:
            self.dis=self.tot*0.5
        self.tot=self.tot-self.dis
        Book.total+=self.tot
    def display(self):
        print(self.__name,end="\t")
        print(self.__author,end="\t")
        print(self.__publisher,end="\t")
        print(self.__price,end="\t")
        print(self.__noc,end="\t")
        print(self.dis,end="\t")
        print(self.tot)      
n=int(input())
books=[]
for i in range(n):
      t=input()
      a=input()
      p=input()
      pr=int(input())
      b=Book(t,a,p,pr)
      noc=int(input())
      b.purchase(noc)
      books.append(b)
print("Bookname Author Publisher price noc discount total")   
for j in books:
    j.display()   
print("No of Books:",len(books))
print("Grand Total:",Book.total)
 
      
      
     
                                 