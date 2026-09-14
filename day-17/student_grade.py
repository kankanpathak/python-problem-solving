class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks >= 50:
            return True
        else:
            return False

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

student1 = Student("Rahul", 78)
student2 = Student("Priya", 92)
student3 = Student("Aman", 45)
student4 = Student("Neha", 65)

print(student1.get_grade())
print(student2.get_grade())
print(student3.get_grade())
print(student4.get_grade())
