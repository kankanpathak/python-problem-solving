n = int(input("Enter number of elements: "))

lst = []

print("Enter elements:")

for _ in range(n):
    lst.append(int(input()))

longest_sequence = []
longest_sum = 0

for i in range(len(lst)):
    current_sequence = []
    current_sum = 0

    for j in range(i, len(lst)):
        current_sequence.append(lst[j])
        current_sum += lst[j]
        if current_sum > 0:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence.copy()
                longest_sum = current_sum

print(f"Longest positive-sum sublist: {longest_sequence}")
print(f"Sum: {longest_sum}")
