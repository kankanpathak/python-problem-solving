num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

total = float("-inf")
row = 0
largest_row = 0

for i in matrix:
    temp_total = 0
    for j in i:
        temp_total += j
    row += 1
    if temp_total > total:
        total = temp_total
        largest_row = row

print(f"Row {largest_row} has the largest sum: {total}")
