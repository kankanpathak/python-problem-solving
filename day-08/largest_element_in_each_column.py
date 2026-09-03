num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

column = 0

for i in range(num_of_elements):
    largest = float("-inf")
    for j in range(len(matrix)):
        if matrix[j][i] > largest:
            largest = matrix[j][i]
    column += 1
    print(f"Column {column} largest: {largest}")
