text = input("Input: ").lower()

my_dict = {}

for char in text:
    if char != " ":
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

print(f"Output: {my_dict}")
