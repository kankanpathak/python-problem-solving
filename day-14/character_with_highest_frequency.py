text = "programming"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

highest_frequency = 0

for value in frequency.values():
    if value > highest_frequency:
        highest_frequency = value

characters = ""

for char, value in frequency.items():
    if value == highest_frequency:
        characters += char + ", "

print(f"Highest frequency: {highest_frequency}")
print(f"Characters: {characters.strip(", ")}")
