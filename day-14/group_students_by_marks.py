students = [
    ["Rahul", 80],
    ["Aman", 70],
    ["Priya", 80],
    ["Neha", 90],
    ["Riya", 70],
    ["Arjun", 90]
]

grouped = {}

for name, marks in students:
    if marks not in grouped:
        grouped[marks] = [name]
    else:
        grouped[marks].append(name)

print(grouped)
