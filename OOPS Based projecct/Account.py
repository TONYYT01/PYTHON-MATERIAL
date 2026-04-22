from abc import ABC,abstractmethod
class BankSystem(ABC):
    AccountNumberCounter=1000
    def __init__(self,data,Amount):
        self.data=data
        self.__Amount=Amount
        BankSystem.AccountNumberCounter+=1
        self.AccountNumber=BankSystem.AccountNumberCounter
    @abstractmethod
    def accountType(self):
        pass
    def withDraw(self,Amount):
        if Amount<500:
            print("Minimum withdraw 500")
        if Amount > self.__Amount:
                print(f"Insuffentx Balance {self.__Amount}")
        self.__Amount-=Amount
        print(f"Account withdrawn sucessfully")
    def deposit(self,Amount):
        if Amount>=100:
            self.__Amount+=Amount
            print(f"Amount deposited sucessfully")
        else:
            print("Deposit only graterthen 100")
    def balance(self):
        return self.__Amount
    def __str__(self):
        return f"Account Number : {self.AccountNumber}\nName : {self.data['Name']} Age : {self.data['Age']}\nEmail : {self.data['Email']}\nAadher : {self.data['AadharNumber']}\nPhone number : {self.data['Phonenumber']}\nBalance : {self.balance()}\nAccount Type : {self.data['AccountType']}"
class SavingsAccount(BankSystem):
    Type="Savings"
    def __init__(self,Data,Amount=0):
        super().__init__(Data,Amount)
        self.accountType()
    def accountType(self):
        print("Savings Account is created")
        print(f"Account Number : {self.AccountNumber}")
class CurrentAccount(BankSystem):
    Type="Current"
    def __init__(self,Data,Amount):
        super().__init__(Data,Amount)
        self.accountType()
    def accountType(self):
        print("Current Account created")
        print(f"Account Number : {self.AccountNumber}")
Accounts={}
user=1
while(user>=1):
    print("1. Create account \n2. Balance check\n3. Withdraw\n4. Deposit\n5.Details\n6. exit")
    k=int(input())
    match(k):
        case 1:
            Name=input("Enter the name : ")
            Age=int(input("Enter your age : "))
            Email=(input("Enter your Email : "))
            AadharNumber=int(input("Enter the Aadhar number : "))
            Phonenumber=int(input("Enter your phone number : "))
            Address=input("Enter your Address  : ")
            data={"Name":Name,"Age":Age,"Email":Email,"AadharNumber":AadharNumber,"Phonenumber":Phonenumber,"Address":Address}
            print("1. Savings Account\n2. Current Account")
            typeinput=int(input())
            match(typeinput):
                case 1:
                    k=int(input("Are you deposite any amount\n1 .Yes\n2.No\n"))
                    Amount=0
                    if k==1:
                        Amount=float(input("Enter the Amount : "))
                    data["AccountType"]=SavingsAccount.Type
                    Account=SavingsAccount(data,Amount)
                    data["Balance"]=Account.balance()
                    Accounts[Account.AccountNumber]=Account
                    print(Accounts)
                case 2:
                    Amount=int(input("Enter the Amount  : "))
                    data["AccountType"]=CurrentAccount.Type
                    Account=CurrentAccount(data,Amount)
                    data["Balance"]=Account.balance()
                    Accounts[Account.AccountNumber]=Account
        case 2:
            Acnumber=int(input("Enter the account Number : "))
            Phnumber=int(input("Enter the phone number : "))
            Account=Accounts.get(Acnumber)
            if Account:
                if Account.data["Phonenumber"]==Phnumber:
                    print(Account.data["Balance"])
                else:
                    print("Invalid phone number")
            else:
                print("Account not found")
        case 3:
            Acnumber=int(input("Enter the Account number : "))
            phnumber=int(input("Enter the phone number : "))
            Account=Accounts.get(Acnumber)
            if Account:
                    if Account.data["Phonenumber"] == phnumber:
                        Amount = float(input("Enter the Amount : "))
                        (Account.withDraw(Amount))
                        Account.data["Balance"]=Account.balance()
                    else:
                        print("Invald phonenumber")
            else:
                print("Account not found")
        case 5:
            Acnumber=int(input("Enter the Account Number : "))
            phnumber=int(input("Enter the phone  Number : "))
            Account=Accounts.get(Acnumber)
            if Account:
                print(Account)
        case 6:
            Acnumber=int(input("Enter the Account Number : "))
            Account=Accounts.get(Acnumber)
            if Account:
                print(Account.data["Name"])
                Userinput=(input("Yes or No"))
                if Userinput=="Yes":
                    print("Transfred")
            else:
                print("Account Not Found")
        case 7:
            user=0
            print("Thank you")
            

