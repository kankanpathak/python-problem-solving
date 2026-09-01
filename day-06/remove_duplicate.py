text = input("Enter a word: ").lower()

new_text = ""

for char in text:
    if char not in new_text:
        new_text += char

print(f"Output: {new_text}")
