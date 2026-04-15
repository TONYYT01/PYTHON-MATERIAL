## Basic intermediate
```python
from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self,Name,Roll_no,Dept,Session,Degree,Address,Email,Course_Status):
        self.Name=Name
        self.Roll_no=Roll_no
        self.Dept=Dept
        self.Session=Session
        self.Degree=Degree
        self.Address=Address
        self.Email=Email
        self.Course_Status=Course_Status
    @abstractmethod
    def Display(self):
        pass
    def Base_Display(self):
        return(
            f"Name            : {self.Name}\n"
            f"Roll No         : {self.Roll_no}\n"
            f"Department      : {self.Dept}\n"
            f"Session         : {self.Session}\n"
            f"Degree          : {self.Degree}\n"
            f"Address         : {self.Address}\n"
            f"Email           : {self.Email}\n"
            f"Course_status   : {self.Course_Status}" 
        )
class Current_Student(Student):
    def __init__(self,Name,Roll_no,Dept,Session,Year_Of_Study,Degree,Address,Email,Course_Status):
        super().__init__(Name,Roll_no,Dept,Session,Degree,Address,Email,Course_Status)
        self.Year_Of_Study=Year_Of_Study
    def Display(self):
        return super().Base_Display()+f"\nYear of Study : {self.Year_Of_Study}"
class Graduate_Student(Student):
    def __init__(self, student, year):
        super().__init__(
            student.Name,
            student.Roll_no,
            student.Dept,
            student.Session,
            student.Degree,
            student.Address,
            student.Email,
            "Completed"   # force status
        )
        self.Year_Of_Completed=year
    def Display(self):
        return super().Base_Display()+f"\nYear of completed : {self.Year_Of_Completed}"
S1=Current_Student("Naveen",2,"CSE","A","IV","B.E","Ongole","Kola@gmail.com","Ongoing")
print(S1.Display())
Gs1=Graduate_Student(S1,2026)
print(Gs1.Display())
```