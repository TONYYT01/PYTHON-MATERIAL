# Table oof the contents

- [Types of Pillers](#types-of-4-pillers)
    - [Encapsulation](#1-encapsulation)
    - [Abstraction](#2-abstraction-hide-complexity)
    - [Inheritance](#3-inheritancereuse-code)

### Types of 4 pillers

- In python or any other language there are totally 4 types of pillers we have 
- With that pillers only we will build the massive systems and the applications are we will design

#### 1 Encapsulation(Data+methods together)

- So the Encapsulation is the one process of wrapping the data and the methods(function) bind together
```python
class Bank_System:
    def __init__(self,balance):
        self.balance=balance
    def Deposit(self,amount):
        self.balance+=amount
    def Balance(self):
        print(self.balance)
A1=Bank_System(1000)
A1.Balance()
A1.Deposit(304)
A1.Balance()
```
- So the above one is the with the help of the amount we performing the some of the operations 
- So the amount behaving the in different ways 
- In deposit is adding the amount to existing the data
- And the balance we will print the balance


#### 2 Abstraction (Hide complexity)

- Abstraction is the process of hideing the complex data
- So we can't directly give access to the user to direct changes in the complex data
- In python we can use the `__` of 2 underScores
- If you put that one to the  variable that will be the private variable
```python
class Bank_System:
    def __init__(self,Name,amount):
        self.__Amount=amount
        self.Name=Name
    def Data(self):
        print(self.__Amount)
A1=Bank_System("KOla",1000)
A1.Data()
```
- So like this we will hide the complexity
- And another Concept is there with the help of abc moduel we will provide the Hide complexity to the method

```python
class Bank_System:
    def __init__(self,Name,amount):
        self.__Amount=amount
        self.Name=Name
    def Data(self):
        print(self.__Amount)
A1=Bank_System("KOla",1000).Name
print(A1)
```
- So we can access the variables by using the normally
- But if you are trying to access the __Amount
it will through the  error 
```python
class Bank_System:
    def __init__(self,Name,amount):
        self.__Amount=amount
        self.Name=Name
    def Data(self):
        print(self.__Amount)
A1=Bank_System("KOla",1000).__Amount
print(A1)
```
```python
 line 7, in <module>
    A1=Bank_System("KOla",1000).__Amount
AttributeError: 'Bank_System' object has no attribute '__Amount'
```

#### 3 Inheritance(Reuse code)
- Inheritance is the process of we Don't want to write the repeated methods again and again with the help of Inheritance we can reuse those thinngs
- In python inheritance is the very simple one and like java it also supports the multipul inheritance also
- It avoids the duplication
```python
class Car:
    def Sound(self):
        print("engine strated")
class Bike(Car):
    pass
v=Bike()
v.Sound()
```
- one class Take the all properties of the another class 
- We call it as the parent class and the child class
- Child class well inherite the properties of the parent and the it has the its own properties
- In this they are types of inheritance is also there we will discuss later
- Types to move ->
- Super keyword

#### 4 Polymorphism(Many forms)
- Same method but different behavior
- It is cleaner code
- Flexibility high
```python
class Dog:
    def Sound(self):
        print("Bark")

class Cat:
    def Sound(self):
        print("Meow")
(Cat().Sound())
(Dog().Sound())
```
- In this some core content is there we will discuss later
- As of now basic level of idea is enough
- core concept -> [Core concept]()

#### [Level 1 concepts](Level1.md)

## [Back-to Basics](OOP.md)