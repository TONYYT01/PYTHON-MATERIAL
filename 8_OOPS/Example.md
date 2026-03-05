## Strong Example code implemented by oops concept
```python
from abc import ABC,abstractmethod
class Bank_System(ABC):
    account_counter=1000
    def __init__(self,data,amount):
        self.data=data
        self.__amount=amount
        Bank_System.account_counter+=1
        self.acc_no=Bank_System.account_counter
    @abstractmethod
    def Account_type(self):
        pass
    def Balance(self):
        print(self.__amount)
    def Details(self):
        print(self.data,self.acc_no)
    def with_draw(self,amount):
        self.__amount-=amount
    def Deposit(self,amount):
        self.__amount+=amount
class Savings_Account(Bank_System):
    def __init__(self,data,amount):
        super().__init__(data,amount)
        self.Account_type()
    def Account_type(self):
        self.type="savings"
        print("Account created")
class Current_Account(Bank_System):
    def __init__(self,data,amount):
        super().__init__(data,amount)
        if amount>500:
            pass
        else:
            raise ValueError("current account atleast 500 deposit")
        self.Account_type()
    def Account_type(self):
        self.type="Current"
        print("Account created")
class Customer_Support:
    def info(self,account):
        account.Details()
details={"First_name":"Naveen","Last_Name":"Kola","PH_NO":8247356197}
try:
    a1=Savings_Account(details,20)
    a1.Details()
    p1=Customer_Support()
    p1.info(a1)
except ValueError as e:
    print(e)
```