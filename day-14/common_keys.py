students_a = {
    "Rahul": 78,
    "Aman": 45,
    "Priya": 92,
    "Neha": 67
}

students_b = {
    "Priya": 88,
    "Neha": 71,
    "Riya": 85,
    "Karan": 56
}

set_a = set(students_a.keys())
set_b = set(students_b.keys())

common_elements = set_a.intersection(set_b)

print(common_elements)
