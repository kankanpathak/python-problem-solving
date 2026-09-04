num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

total = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0 or i == num_of_rows - 1 or j == 0 or j == num_of_elements - 1:
            total += matrix[i][j]

print(f"Border sum: {total}")
