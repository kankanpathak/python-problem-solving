class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        self.__salary += amount

class Manager(Employee):
    def __init__(self, name,salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        return f"{self.name} is a manager of {self.department} department with salary {self.get_salary()}."


manager = Manager("Kankan", 50000, "IT")

manager.increase_salary(10000)

print(manager.display_info())
