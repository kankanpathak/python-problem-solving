sentence = "python is easy python is powerful python is easy"

frequency = {}

unique_words = set()
repeated_words = set()

for word in sentence.split():
    if word in frequency:
        frequency[word] += 1
        repeated_words.add(word)
    else:
        frequency[word] = 1
        unique_words.add(word)

print(f"Unique words: {unique_words}")
print(f"Number of unique words: {len(unique_words)}")
print(f"Repeated words: {repeated_words}")
