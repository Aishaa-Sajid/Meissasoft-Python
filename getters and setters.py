class Account:
    def __init__(self,acc_no,acc_pass,balance):
        self.acc_no=acc_no
        self._balance=balance
        self.__acc_pass=acc_pass

    def debit(self,amount):
        if amount<0:
            print("Debit amount must be positive!")
        else:
            if(self._balance==0 or self._balance < amount):
                print("You cannot make this operation, balance is 0")
            else:
                self._balance-=amount
                print(f"Rs.{amount} was debited")
                print("Total balance =", self.balance)

    def credit(self,amount):
        if amount<0:
            print("Credit amount must be positive!")
        else:
            self._balance+=amount
            print(f"Rs.{amount} was credited")
            print("Total balance =", self.balance)
    
    @property       #@property turns a method into a “managed attribute”.
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,value):
        if value>=0:
            self._balance=value
        else:
            print("VAlue cannot be less than zero")

    
    
obj=Account("12345","abcde",0)
# obj.balance=-1000
# obj.credit(2000)
# obj.debit(-1000)
obj.debit(1000)


