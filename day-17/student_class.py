class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}\nMarks: {self.marks}")


Student1 = Student("Rahul", 78)
Student1.display_info()

Student2 = Student("Priya", 92)
Student2.display_info()
