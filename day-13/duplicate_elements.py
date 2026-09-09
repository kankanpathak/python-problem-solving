numbers = [1, 2, 3, 2, 4, 5, 3, 6, 2, 7]

seen = set()
duplicates = []

for i in numbers:
    if i in seen and i not in duplicates:
        duplicates.append(i)
    else:
        seen.add(i)

print(duplicates)
