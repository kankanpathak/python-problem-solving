n = int(input("Enter number of elements: "))

lst = []

print("Enter elements:")

for _ in range(n):
    lst.append(int(input()))

current_num = lst[0]
current_sequence = [current_num]
longest_sequence = []

for i in range(1, len(lst)):
    current_num = lst[i]

    if lst[i] not in current_sequence:
        current_sequence.append(current_num)
    
    else:
        for j in range(len(current_sequence)):
            if current_sequence[j] == current_num:
                new_sequence = []
                for k in range(j+1, len(current_sequence)):
                    new_sequence.append(current_sequence[k])
                current_sequence = new_sequence
                current_sequence.append(current_num)
                break

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence.copy()

if len(current_sequence) > len(longest_sequence):
    longest_sequence = current_sequence.copy()

print(f"Longest sublist with not repeated elements: {longest_sequence}")
