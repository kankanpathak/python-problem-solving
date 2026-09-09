students = [
    ["Rahul", 78],
    ["Aman", 45],
    ["Priya", 92],
    ["Neha", 67],
    ["Riya", 45]
]

student_marks = {}

for name, marks in students:
    student_marks[name] = marks

print(student_marks)

print()
for name, marks in student_marks.items():
    print(f"{name} -> {marks}")

print()
for name, marks in student_marks.items():
    if marks >= 60:
        print(f"{name} -> {marks}")

print()
for name, marks in student_marks.items():
    if name == 'Priya':
        print(f"Priya got {marks}")

