text = input("Enter a word: ").lower()

my_dict = {}

for char in text:
    if char != " ":
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

first_non_repeating_char = "Not found"

for key, value in my_dict.items():
    if value == 1:
        first_non_repeating_char = key
        break

print(f"Output: {first_non_repeating_char}")
