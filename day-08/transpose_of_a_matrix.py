num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

transpose = []

for i in range(num_of_elements):
    lst = []
    for j in range(len(matrix)):
        lst.append(matrix[j][i])
    transpose.append(lst)

print(f"Original:\n{matrix}\n")
print(f"Transpose:\n{transpose}")
