n = int(input("Enter number of elements: "))

lst = []

print("Enter elements of first list:")

for _ in range(n):
    lst.append(int(input()))

current_num = lst[0]
current_sequence = [current_num]
longest_sequence = []

for i in range(1, len(lst)):
    previous_num = current_num
    current_num = lst[i]

    if current_num == previous_num + 1:
        current_sequence.append(current_num)
        previous_num = current_num
    
    else:
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
        current_sequence = [current_num]

if len(current_sequence) > len(longest_sequence):
    longest_sequence = current_sequence

print(f"Longest sequence: {longest_sequence}")
