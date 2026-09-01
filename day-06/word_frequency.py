text = input("Enter a sentence: ").lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")

my_dict = {}

for word in text.split():
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

print(f"Output: {my_dict}")
