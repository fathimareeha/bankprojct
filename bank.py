import random
class MyBank:
    def __init__(self,frstnme,lstnme,adrs,place,amount):
        self.frstnme=frstnme
        self.lstnme=lstnme
        self.adrs=adrs
        self.place=place
        self.amount=amount
        self.acntnmbr=random.randint(0000,9999)
        
    
    def customer(self):
        print("First name=",self.frstnme,"Last name=",self.lstnme,"Address=",self.adrs,"Place=",self.place,"Amount=",self.amount,"Account number=",self.acntnmbr)
       
    def withdraw(self,withdraw):
        if self.amount>0:
            if 0<withdraw<50000:
                amount=self.amount-withdraw
                print("Amount after withdraw=",amount)
            else:
                print("can't withdraw more than 50000")
        else:
            print("no balance")
    def deposit(self,deposit):
        amount=self.amount+deposit
        print("Amount after deposit=",amount)
        
        
myobj=MyBank("fathima","reeha","darulhidaya","kuthupramba",100000)
myobj.customer()
print("1.withdraw","2.deposit")
option=int(input("choose the option"))
if option==1:
    
    withdraw=int(input("enter the amount to withdraw"))
  
    myobj.withdraw(withdraw)
elif option==2:
    deposit=int(input("enter the amount to deposit"))
    myobj.deposit(deposit)

