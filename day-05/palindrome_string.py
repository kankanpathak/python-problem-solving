text = input("Enter a word: ").lower()

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
