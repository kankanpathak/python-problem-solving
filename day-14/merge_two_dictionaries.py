marks1 = {
    "Rahul": 78,
    "Aman": 45,
    "Priya": 92
}

marks2 = {
    "Neha": 67,
    "Riya": 85,
    "Karan": 56
}

merged = {}

for name, marks in marks1.items():
        merged[name] = marks

for name, marks in marks2.items():
        merged[name] = marks

print(merged)
