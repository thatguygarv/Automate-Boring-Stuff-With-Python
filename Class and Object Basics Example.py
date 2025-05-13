class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def display(self):
        print(f"{self.name}'s GPA is {self.gpa}")

s1 = Student("Garv", 6.9)
s1.display()
