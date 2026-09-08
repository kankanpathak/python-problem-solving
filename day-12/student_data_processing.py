students = [
    ["Rahul", 78],
    ["Aman", 45],
    ["Priya", 92],
    ["Neha", 67],
    ["Riya", 45],
    ["Arjun", 92],
    ["Karan", 56]
]

highest_score = 0
lowest_score = 100
total_marks = 0
student_count = 0

for name, marks in students:
    if marks > highest_score:
        highest_score = marks

    if marks < lowest_score:
        lowest_score = marks

    total_marks += marks
    student_count += 1

for name, marks in students:
    if marks == highest_score:
        print(f"Highest: {name} -> {marks}")
        break

for name, marks in students:
    if marks == lowest_score:
        print(f"Lowest: {name} -> {marks}")
        break

print(f"Average: {total_marks / student_count:.2f}")

print("Student who passed:")
for name, marks in students:
    if marks >= 50:
        print(name)

for i in range(len(students)):
    for j in range(i+1, len(students)):
        if students[i][1]== students[j][1]:
            print(f"{students[i][1]} -> {students[i][0]}, {students[j][0]}")

