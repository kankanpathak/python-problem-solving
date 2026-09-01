first_text = input("Enter first word: ").lower()
second_text = input("Enter second word: ").lower()

first_dict = {}
second_dict = {}

for char in first_text:
    if char != " ":
        if char in first_dict:
            first_dict[char] += 1
        else:
            first_dict[char] = 1

for char in second_text:
    if char != " ":
        if char in second_dict:
            second_dict[char] += 1
        else:
            second_dict[char] = 1

if first_dict == second_dict:
    print("Anagram")
else:
    print("Not an Anagram")
