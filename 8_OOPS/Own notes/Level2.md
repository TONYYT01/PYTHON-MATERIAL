### Table contents
- [Method Overloading](#method-overloading)
- [Method Overriding](#method-overridding)
- [Multiple inheritanece]()
- [MRO method resolution order]()

#### Method overloading
- This method overloading is the same method name different parameters
- Actually reality python does not support it
```python
class Solve:
    def Add(self,n1,n2):
        return n1+n2
    def Add(self,n1):
        return n1*1
print(Solve().Add(2))
print(Solve().Add(2,8))

```
- Python does not support method overloading but we can achive that one by the default arguments
```python
class Test:
    def Add(slef,n1,n2=0):
        return n1+n2
print(Test().Add(2,9))
print(Test().Add(2))
```

### Method overridding

- Method overridding is the one of the process when the child class Modifies the parent calss method
- So That is method overridding 
- We are override the method of the parent class what he has with help of child class
- This entair process is done by only the it inherite the class
```python
class A:
    def Mooment(self):
        print("I Started the car")
class B(A):
    def Mooment(self):
        print("I Stoped the car")
(B().Mooment())
```
- Above one doing without you started the car it will stoped the car
- But in reality not like that right
- Actully we can do that proper one by using one thing see the below code
```python
class A:
    def Mooment(self):
        print("I started the Car")
class B(A):
    def Mooment(self):
        super().Mooment()
        print("I Stoped the Car")
(B().Mooment())
```
- `super` is a keyword by using that one we can do 
- It represent the parent class Always

