## Table of the contents

- [Importance of the __init__](#importance-of-the-init)
- [Self-Key word](#self)
- [Instance and class Variables](#instance-and-class-variables)
- [Types of Methods](#types-of-methods)
### Importance of the __init__

- So this is an in built function
- It runs automatically when ever the object is created
- With the help one only we can build the larger applications
```python
class Bank_System:
    def __init__(self,Name,Amount):
        self.name=Name
        self.__Amount=Amount
    def Data(self):
        print(f"{self.__Amount} {self.name}")
A1=Bank_System("Naveen",10000)
(A1.Data())
```
- The process is when you stracture the class that will under the init that will class creation
- So the when you created the object that will be automatically like this
```python
1. Create object ->A1=Back_System("Tony",20000)
2. Call __init__(A1, "Tony", 20000)
3. Assign values
```
- Like above one it processing the all those things actully

### Self
- So self is reference to the current object
- So what is that current object?
- The current object will be the when the object is created and you know the python automatically run the __init__ on right so when that object is created it automatically references to tha values to there pirticular things
```python
class Bank_System:
    def __init__(self,name,Amount):
        self.name=name
        self.__Amount=Amount
    def Data(self):
        print(f"{self.name},{self.__Amount}")
a1=Bank_System("Name",20000)
a1.Data()
a2=Bank_System("Tony",9876787)
a2.Data()

```
- So above example each object has its own data
- That actully possible by the `self` keyword only

## Instance and class Variables

- so this two are the variable  declaration and using that data into our project ,program

#### Instance Variable
- Unique for each object
- So this instance variable are the personal data containers
```python
class Bank_System:
    def __init__(self,name):
        self.name=name
s1=Bank_System("Kola")
s2=Bank_System("Naveen")
print(s1.name)
print(s2.name)
```
- In this s1.name!=s2.name

### Class Variables
- Shared by all objects
- So this variables are the access in the all object
- So this is like common data 
```python
class Bank_System:
    Bank_name="SBI"
    def __init__(self,name):
        self.name=name
    def Data(self):
        print(Bank_System.Bank_name,self.name)
a1=Bank_System("Naveen")
a2=Bank_System("TONY")
a1.Data()
a2.Data()
```
- you have to observe hear there is something good
- In the class we have the class Variable is Bank_name
- When you created the 2 objects and the getting data
- The data function of each one will have there print bank_name and the name of that person 
- Name is different but the Bank_name is same for if the bank has the 1m accounts its not be changed
- We can Access that one like this 
```python
class Bank_System:
    Bank_name="SBI"
    def __init__(self,name):
        self.name=name
    def Data(self):
        print(Bank_System.Bank_name,self.name)
a1=Bank_System("Naveen")
a2=Bank_System("TONY")
print(a1.Bank_name)
print(Bank_System.Bank_name)
```


- One confusion clarity
```python
class Bank_System:
    Bank_name="SBI"
    def __init__(self,name):
        self.name=name
    def Data(self):
        print(Bank_System.Bank_name,self.name)
a1=Bank_System("Naveen")
a2=Bank_System("TONY")
a1.Bank_name="Canara"
print(a1.Bank_name)
print(Bank_System.Bank_name)
```
- In above program you might be think class Variabel value changed 
- But not when you do that it will create the instance variable
- Not be class Variable changed

### Types of methods
- This are the decoraters used in our python
- Instance methood
- Class method
- Static method

### Instance method

- The instance method is used we are working on the Object data like instance variable
```python
class Bank_System:
    def __init__(self,name,Amount):
        self.name=name
        self.Amount=Amount
    def Data(self):
        print(self.name,self.Amount)
A1=Bank_System("Naveen",1234)
(A1.Data())
```
### Class Methods
- This class methods is used and working on the class Variables
- By using the `@classmethod` we can declare in the python
```python
class Bank_system:
    Account_Number=1000
    def __init__(self,name,Amount):
        self.name=name
        self.Amount=Amount
        Bank_system.Account_Number+=1
        self.Account_num=Bank_system.Account_Number
    @classmethod
    def Data(self):
        print(self.Account_Number)
A1=Bank_system("Naveen",2432)
A2=Bank_system("Naveen",2432)
A3=Bank_system("Naveen",2432)
A4=Bank_system("Naveen",2432)
A4.Data()
```
### Static method
- This is like no data only logic it will work
```python
class Bank_System:
    def __init__(self,name,Amount):
        self.name=name
        self.Amount=Amount
    @staticmethod
    def Check(amount):
        return amount>0
    def Data(self):
        print(self.name,self.Amount)
name=input()
Amount=float(input())
if Bank_System.Check(Amount):
    Account=Bank_System(name,Amount)
    Account.Data()
else:
    print("Check the amount you are entering")
```

- [Level 2 ->](Level2.md)