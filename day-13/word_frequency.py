sentence = "python is easy and python is powerful and python is popular"

frequency = {}

for word in sentence.split():
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

highest_frequency = 0
most_frequent_word = ""

for key, value in frequency.items():
    if value > highest_frequency:
        highest_frequency = value
        most_frequent_word = key

print(f"Most frequent word: {most_frequent_word}")
print(f"Frequency: {highest_frequency}")
