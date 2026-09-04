num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

search = int(input("Enter which number you want to search: "))

row = 0
column = 0
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if search == matrix[i][j]:
            row = i+1
            column = j+1
            found = True
            break
    if found:
        print(f"Found {search} at Row {row}, Column {column}")
        break
else:
    print("Number not found")
