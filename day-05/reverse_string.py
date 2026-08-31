text = input("Enter a word: ")

reverse = ""

for char in text:
    reverse = char + reverse

print(f"Reverse: {reverse}")
