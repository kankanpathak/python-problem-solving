num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

row = 0

for i in matrix:
    total = 0
    for j in i:
        total += j
    row += 1
    print(f"Row {row} sum: {total}")
