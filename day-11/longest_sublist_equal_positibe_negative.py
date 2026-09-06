n = int(input("Enter number of elements: "))

lst = []

print("Enter elements:")

for _ in range(n):
    lst.append(int(input()))

longest_sequence = []

for i in range(len(lst)):
    current_sequence = []
    positive_count = 0
    negative_count = 0

    for j in range(i, len(lst)):
        current_sequence.append(lst[j])

        if lst[j] > 0:
            positive_count += 1
        elif lst[j] < 0:
            negative_count += 1

        if positive_count == negative_count and positive_count > 0:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence.copy()

print(f"Longest sublist with equal positive and negative numbers: {longest_sequence}")
