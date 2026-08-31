text = input("Enter a word: ")

total_char = 0
letters = 0
digits = 0

for char in text:
    total_char += 1

    if char.isalpha():
        letters += 1
        
    elif char.isdigit():
        digits += 1

print(f"Total Characters: {total_char}")
print(f"Letters: {letters}")
print(f"Digits: {digits}")
