n = int(input("Enter number of elements: "))

lst = []

print("Enter elements:")

for _ in range(n):
    lst.append(int(input()))

current_num = lst[0]
current_sequence = [current_num]
longest_sequence = []
previous_direction = ""

for i in range(1, len(lst)):
    previous_num = current_num
    current_num = lst[i]
    direction = ""

    if current_num > previous_num:
        direction = "up"
    else:
        direction = "down"

    if previous_direction != direction:
        current_sequence.append(lst[i])
        previous_direction = direction
    else:
        current_sequence = [previous_num, current_num]
        previous_direction = direction

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence.copy()

if len(current_sequence) > len(longest_sequence):
    longest_sequence = current_sequence.copy()

print(f"Longest alternating sublist: {longest_sequence}")
