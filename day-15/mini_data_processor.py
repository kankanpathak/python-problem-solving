students = [
    ["Rahul", 78],
    ["Aman", 45],
    ["Priya", 92],
    ["Neha", 67],
    ["Riya", 45],
    ["Arjun", 92],
    ["Karan", 56]
]


def find_top_student(students):
    top_student = ""
    highest_marks = 0

    for name, marks in students:
        if marks > highest_marks:
            highest_marks = marks
            top_student = name

    return f"Top student: {top_student}"


def find_average_marks(students):
    total = 0
    count = 0

    for name, marks in students:
        total += marks
        count += 1

    return f"Average: {(total / count):.2f}"


def find_passed_students(students):
    passed_students = []

    for name, marks in students:
        if marks >= 50:
            passed_students.append(name)

    return f"Passed students: {passed_students}"


def find_duplicate_marks(students):
    frequency_of_marks = {}
    duplicate_marks = []

    for name, marks in students:
        if marks in frequency_of_marks:
            frequency_of_marks[marks] += 1
        else:
            frequency_of_marks[marks] = 1

    for marks, frequency in frequency_of_marks.items():
        if frequency > 1:
            duplicate_marks.append(marks)

    return f"Duplicate marks: {duplicate_marks}"

print(find_top_student(students))
print(find_average_marks(students))
print(find_passed_students(students))
print(find_duplicate_marks(students))
