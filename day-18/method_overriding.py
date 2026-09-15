class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I study {self.course}."

student = Student("Rahul", 21, "Python")
print(student.introduce())
