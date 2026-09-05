n1 = int(input("Enter number of elements of first list: "))

list1 = []

print("Enter elements of first list:")

for _ in range(n1):
    list1.append(int(input()))

n2 = int(input("Enter number of elements of second list: "))

list2 = []

print("Enter elements of second list:")

for _ in range(n2):
    list2.append(int(input()))


new_list = []

for i in list1:
    for j in list2:
        if i == j:
            if j not in new_list:
                new_list.append(j)

print(f"New list: {new_list}")
