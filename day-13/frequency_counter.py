numbers = [4, 2, 4, 3, 2, 4, 5, 3, 2]

frequency = {}

for i in numbers:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1

print(frequency)
