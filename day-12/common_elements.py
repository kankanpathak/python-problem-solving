list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

new_list = []

for i in list1:
    for j in list2:
        if j == i:
            new_list.append(j)

print(new_list)
