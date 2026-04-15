## Table of the contents

- [Dunder (Magical) Methods](#dunder-methods)
- [Abstraction (real way,not theory)](#abstraction-real-way)
### Dunder Methods
- So the dender methods are start and ends with the `__`. They only define how the object will behave

#### Most importent Methods

1. `__init__`
    - Already you know the importance of this dunder method.It runs automatically whenever the object is created 
    ```python
    class Student:
    def __init__(self,Name):
        self.name=Name
    S1=Student("Naveen")
    print(S1)
    ```
    - O/p -> `<__main__.Student object at 0x000001C9CCEBE9D0>`
2. `__str__`
    - This method will give or provide the string representation to the object
    - Controls what get print
    ```python
    class Student:
    def __init__(self,Name):
        self.Name=Name
    def __str__(self):
        return f"My name is {self.Name}"
    S1=Student("Naveen")
    print(S1)
    ```
    - Actually above is the one of the way but in before we will do that one differently
    ```python
    class Student:
    def __init__(self,Name):
        self.Name=Name
    def Data(self):
        return f"My name is {self.Name}"
    S1=Student("Naveen")
    print(S1.Data())
    ```
    - above one is one of the way may we will use this one only i think so mostly
3. `__len__`
    ```python
    class Student:
    def __init__(self,value):
        self.value=value
    def __len__(self):
        c=0
        for i in self.value:
            c+=1
        return c
    S1=Student("kola")
    print(len(S1))
    ```
4. `__add__`
    - This  is work like the `+`
    - So by using this one we should perform the mathamatical operation
    ```python
    class Student:
    def __init__(self,number):
        self.number=number
    def __add__(self,number2):
        return self.number+number2.number
    n1=Student(10)
    n2=Student(20)
    print(n1+n2)
    ```
- so this are so importent dunder methods

### Abstraction (Real way)
- We will do the real abstraction by using the ABC(abstract base class)
- So in before you are seen that one is very small one 
- you will see the real implementation of the abstarction
- It is like define the rules to the child class must follw
```python
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def Start(self):
        pass
v=vehicle()
print(v)-> throw error
```
- It will through the error because of the dude i declare the abstract method but my self i can't use that one but some like my child it can use 
- Like that it will define it
```python
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def Start(self):
        pass
class Car(vehicle):
    def Start(slef):
        print("Started")
c=Car()
c.Start()
```
#### Question rise what is the use of i defing like this 
- That is it forced to define the start method
- Because we need complesery each vehicle needed the start method that's why we neeed the abstract method
- “Bro, you didn’t implement Start() — not allowed.” like that it will define
- Abstraction is implemented using abstract classes, where abstract methods must be defined by child classes.

### Design Thinking
- (someone)it is a real skill actually dude so if someone ask you are ready to to build the system by using the oop's
- (me)Yes ofcourse
- (someone)Then Build the students system
- (someone)not like this
```python
name="Naveen"
age=21
Class="CSE-A"
```
- (me)No no i will do that one in magically no problem i will take care of it see the Below

### [check the practice codes -> ](Practicedoopscodes.md)