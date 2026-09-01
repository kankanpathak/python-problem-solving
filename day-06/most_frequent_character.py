text = input("Enter a word: ").lower()

my_dict = {}

for char in text:
    if char != " ":
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

count = 0
most_frequent_char = ""

for key, value in my_dict.items():
    if value > count:
        count = value
        most_frequent_char = key

print(f"Most frequent character: {most_frequent_char}")
print(f"Count: {count}")
