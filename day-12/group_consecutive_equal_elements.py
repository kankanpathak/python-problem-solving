numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]

result = []
current_group = [numbers[0]]

for i in range(1, len(numbers)):
    previous_num = numbers[i - 1]
    current_num = numbers[i]

    if current_num == previous_num:
        current_group.append(current_num)
    else:
        result.append(current_group)
        current_group = [current_num]

result.append(current_group)

print(result)
