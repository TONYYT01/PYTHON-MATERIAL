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
### Another One strong example

```python
from abc import ABC,abstractmethod
class Bank_System(ABC):
    account_counter=0
    def __init__(self,data,amount=0):
        self.data=data
        self.__amount=amount
        Bank_System.account_counter+=1
        self.acc_NO=Bank_System.account_counter
    @abstractmethod
    def Account_type(self):
        pass
    def WithDraw(self,amount):
        if self.__amount>=amount:
            self.__amount-=amount
            print("Money Credited sucessfully")
        else:
            print("Insuffent Balance")
    def Deposit(self,amount):
        self.__amount+=amount
        print("Money deposited sucessfully")
    def Balance(self):
        print(self.__amount)
class Savings_Account(Bank_System):
    def __init__(self,data,amount):
        super().__init__(data,amount)
        self.Account_type()
    def Account_type(self):
        self.type="savings"
        print("Savings Account Created \nAccount Number : ",self.acc_NO)
class Current_Account(Bank_System):
    def __init__(self,data,amount):
        super().__init__(data,amount)
        if amount>=500:
            pass
        else:
            raise ValueError("Please Enter the amount above 500")
        self.Account_type()
    def Account_type(self):
        self.type="Current"
        print("Current Account Created \n Account Number : ",self.acc_NO)
ui=1
accounts={}
while(ui>0):
    print("1.Account_Create\n2.With_Draw\n3.Deposit\n4.Balance\n5.0 to exit")
    ui=int(input())
    match(ui):
        case 1:
            First_Name=input("Enter your First name : ")
            last_name=input("Enter your last name : ")
            phone_no=int(input("Enter your phone number : "))
            data={"First_Name":First_Name,"Last_Name":last_name,"Phone_Number":phone_no}
            print("IF you want to add the money")
            print("1.Yes\n2.No")
            money_choise=int(input())
            if money_choise==1:
                money=float(input("Enter the amount : "))
            else:
                money=0
            print("1.Savings Account\n2.Current Account")
            ty=int(input())
            if ty==1:
                New_account=Savings_Account(data,money)
            else:
                if money>500:
                    New_account=Current_Account(data,money)
                else:
                    while(money<500):
                        money=float(input("Enter the money above 500 : "))
                    New_account=Current_Account(data,money)
            accounts[New_account.acc_NO]=New_account
        case 2:
            Account_number=int(input("Enter the Account Number"))
            if Account_number in accounts:
                user=accounts[Account_number]
                print("Security reasons enter the phone number ")
                phone_number=int(input("Enter the Phone number : "))
                if user.data["Phone_Number"]==phone_number:
                    money=float(input("Enter the money : "))
                    user.WithDraw(money)
                else:
                    print("Invalid phone number")
            else:
                print("Account not found")
        case 3:
            Account_number=int(input("Enter the account_number : "))
            if Account_number in accounts:
                user=accounts[Account_number]
                phone_number=int(input("Enter the phone number : "))
                if user.data["Phone_Number"]==phone_number:
                    money=float(input("Enter the amount : "))
                    user.Deposit(money)
                else:
                    print("Enter valid phone number : ")
            else:
                print("Account not found")
        case 4:
            Account_number=int(input("Enter the Account Number : "))
            if Account_number in accounts:
                user=accounts[Account_number]
                phone_number=int(input("Enter  the phone number : "))
                if user.data["Phone_Number"]==phone_number:
                    user.Balance()
                else:
                    print("Enter the Valid phone number")
            else:
                print("account not found")
        case 5:
            ui=0
            print("Bye")

```



## OOPS WITH FILEs  HANDLING

```python
from abc import ABC,abstractmethod
import os
last_number=0
if os.path.exists("Accounts.txt"):
            with open("Accounts.txt","r") as file:
                lines=file.readlines()
                for line in reversed(lines):
                    if "Account Number" in line:
                        num=int(line.split(":")[1])
                        last_number=num
                        break
class Bank_System(ABC):
    Accountnumber_count=last_number
    def __init__(self,data,amount=0):
        self.data=data
        self.__amount=amount
        Bank_System.Accountnumber_count+=1
        self.Acc_no=Bank_System.Accountnumber_count
    @abstractmethod
    def Account_Type(self):
        pass
    def WithDraw(self,amount):
        if self.__amount>=amount:
            self.__amount-=amount
        else:
            raise ValueError("Insuffent balance")
    def Balance(self):
        return self.__amount
    def Deposit(self,amount):
        self.__amount+=amount
class Savings_Account(Bank_System):
    def __init__(self,data,amount=0):
        super().__init__(data,amount)
        self.Account_Type()
    def Account_Type(self):
        self.type="Savings"
        print(f"{self.type} Account_Created \nAccount_number = {self.Acc_no}")
class Current_Account(Bank_System):
    def __init__(self,name,amount):
        super().__init__(name,amount)
        if amount>=500:
            pass
        else:
            raise ValueError("Deposit min 500")
        self.Account_Type()
    def Account_Type(self):
        self.type="Current"
        print(f"{self.type} Account_Created \nAccount_number = {self.Acc_no}")
ui=1
while(ui>0):
    print("1.Account_Create\n2.With_Draw\n3.Deposit\n4.Balance\n5.0 to exit")
    ui=int(input())
    match(ui):
        case 1:
            First_Name=input("Enter your First name : ")
            last_name=input("Enter your last name : ")
            phone_no=int(input("Enter your phone number : "))
            data={"First_Name":First_Name,"Last_Name":last_name,"Phone_Number":phone_no}
            print("IF you want to add the money")
            print("1.Yes\n2.No")
            money_choise=int(input())
            if money_choise==1:
                money=float(input("Enter the amount : "))
            else:
                money=0
            print("1.Savings Account\n2.Current Account")
            ty=int(input())
            if ty==1:
                New_account=Savings_Account(data,money)
            else:
                if money>500:
                    New_account=Current_Account(data,money)
                else:
                    while(money<500):
                        money=float(input("Enter the money above 500 : "))
                    New_account=Current_Account(data,money)
            with open("Accounts.txt","a+") as file:
                    acc=New_account
                    file.write(f"Account Number : {acc.Acc_no}\n")
                    file.write(f"Name : {acc.data['First_Name']} {acc.data['Last_Name']}\n")
                    file.write(f"Type : {acc.type}\n")
                    file.write(f"Balace : {acc.Balance()}\n")
                    file.write("___________________________\n")
            print("Data Saved")
        case 3 :
            account_number=int(input("Enter the accounnt number : "))
            ok=False
            with open("Accounts.txt","r") as file:
                lines=file.readlines()
                for i,line in enumerate(lines):
                    if "Account Number" in line:
                        num=int(line.split(":")[1].strip())
                        if num==account_number:
                            ok=True
                            balance_line=i+3
                            balance=float(lines[balance_line].split(":")[1].strip())
                            amount=float(input("Enter the amount : "))
                            balance+=amount
                            lines[balance_line]=f"Balance : {balance}\n"
                            break
            if not ok:
                print("Not found")
            else:
                with open ("Accounts.txt","w") as file:
                    file.writelines(lines)
                print("Deposited sucessfully")
        case 2:
            Account_number=int(input("Enter the Account Number : "))
            ok=False
            with open("Accounts.txt","r") as file:
                lines=file.readlines()
                for i,line in enumerate(lines):
                    if "Account Number" in line:
                        num=int(line.split(":")[1].strip())
                        if num==Account_number:
                            ok=True
                            balance_line=i+3
                            balance=float(lines[balance_line].split(":")[1].strip())
                            amount=float(input("Enter the Amount : "))
                            if balance>=amount:
                                balance-=amount
                                lines[balance_line]=f"Balance : {balance}\n"
                            else:
                                print("Insuffent balamce")
                                ok=False
                            break
            if not ok:
                print("Not found")
            else:
                with open("Accounts.txt","w") as file:
                    file.writelines(lines)
                print("withdraw sucessfully")


            
```