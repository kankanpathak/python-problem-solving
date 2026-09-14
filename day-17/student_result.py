class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks >= 50:
            return True
        else:
            return False


Student1 = Student("Rahul", 78)
print(Student1.is_passed())

Student2 = Student("Aman", 45)
print(Student2.is_passed())

Student3 = Student("priya", 92)
print(Student3.is_passed())

Student4 = Student("Neha", 38)
print(Student4.is_passed())
